from fastapi import APIRouter
from db.models.attendance import  AttendanceUser, EmployeeModel,Otp,CompanyModel
from apps.attendance_system.schemas.attendance import AttendanceTodayDetailModel,Company,CompanyInvitation
from db.models.attendance import Otp
from requests import Session
from db.session import get_db
from fastapi import Depends, HTTPException, Request,status,UploadFile,Form,File
from db.repository.attendance_repo import AttendanceRepo
from apps.attendance_system.route_login import get_current_user_from_token,get_current_user_from_bearer
from pydantic import BaseModel,root_validator
from typing import Optional
from schemas.attendance import Status
from datetime import date, datetime, time, timedelta
from upload_file import firebase_upload
import json
import os


router =APIRouter(include_in_schema=True,prefix='/api/v1/employee',tags=['Employee'])
class Invitations(BaseModel):
    id:int
    company:Company 
    is_accepted:bool
    is_invited:bool
    status:Status=None
    class Config:
        orm_mode=True
class EmployeeCompanies(BaseModel):
    invitations:list[Invitations]
    active:list[Invitations]
    inactive:list[Invitations]
    class Config:
        orm_mode=True   

class EmployeeProfile(BaseModel):
    name:Optional[str] 
    email:Optional[str]
    dob:date
    @classmethod
    def __get_validators__(cls) :
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls,value): 
        if isinstance(value,str):
            return cls(**json.loads(value))
        return value   
    class Config:
        orm_mode=True
@router.post('/get-today-details')#,response_model=AttendanceTodayDetailModel)
async def get_today_details(companyId:int,current_user:AttendanceUser=Depends(get_current_user_from_bearer),db: Session = Depends(get_db)):
    employee=AttendanceRepo.get_employee(current_user.phone,db)
    today_details=AttendanceRepo.get_today_details(employeeId=employee.id,db=db,companyId=companyId)
    return today_details  


     
@router.get('/profile')
async def getProfile(current_user:AttendanceUser=Depends(get_current_user_from_bearer),db: Session = Depends(get_db)):
    return current_user




@router.post('/update-profile')
async def updateProfile(profile:EmployeeProfile=Form(...),photo:UploadFile(...)=File(None),current_user:AttendanceUser=Depends(get_current_user_from_bearer),db: Session = Depends(get_db)):
    profiledict=profile.__dict__
    if photo:
        url=None 
        
        try:
            # if len(await file.read()) >= 8388608:
            #     return {"Your file is more than 8MB"}
            contents = photo.file.read()

            ext=photo.filename.split(".")[-1]
            url =firebase_upload(contents,ext,photo.filename)
            print(url)
        except Exception as e:
            print(e)
            return e
        photoUrl=None
        
        if url:
            profiledict['photoUrl']=url

    
    updatedUser=AttendanceRepo.update_user(current_user.id,db,profiledict)
    
    return current_user
    
@router.get('/accept-invitations/{id}',response_model=Invitations)
async def accept_invitations(id:int,current_user:AttendanceUser=Depends(get_current_user_from_bearer),db: Session = Depends(get_db)):
    invitation= AttendanceRepo.updateInvitation(id,db)

    return invitation
     


@router.post('/login')
async def login(phone:int, db: Session = Depends(get_db)):
    employee=AttendanceRepo.get_employee(phone,db)
    if   employee is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Employee does not exist.")
    else:
        user=AttendanceRepo.get_user(phone,db)
        if not user:
            AttendanceRepo.create_user(phone,db)
        otp=AttendanceRepo.create_otp(phone,db)
        return {"otp":otp.code}
 

@router.post('/verify-otp')
async def verifyOtp(phone,otp:str,db: Session = Depends(get_db)):
    
   return AttendanceRepo.verify_otp(otp,phone,db)
@router.get('/companies'  ,response_model=list[Invitations])
async def get_companies(current_user:AttendanceUser=Depends(get_current_user_from_bearer),db: Session = Depends(get_db)):
    
    if current_user.is_employer:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Not Authorized.")
    employee=AttendanceRepo.get_employee(phone=int(current_user.phone),db=db)
    allInvitations=AttendanceRepo.getInvitationByCompany(employee.id,db)
    return allInvitations

class InvitationsResponse(BaseModel):
    invitations:list[Invitations]
    class Config:
        orm_mode=True
@router.get('/invitations',response_model=list[Invitations])
async def get_invitations(current_user:AttendanceUser=Depends(get_current_user_from_bearer),db: Session = Depends(get_db)):
    employee=AttendanceRepo.get_employee(phone=current_user.phone,db=db)
    allInvitations=AttendanceRepo.getInvitationByCompany(employee.id,db)
    return  allInvitations

@router.post('attendance-store')
async def store_attendance():
    return {
        
    }
@router.post('start-break-submit')
async def store_break_start():

    return {}


@router.post('brek-end-submit')
async def store_break_end():
    return {}


