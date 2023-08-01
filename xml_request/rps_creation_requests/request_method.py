
from schemas.users import AcPayBankListRequest, CancelTransactionRequest, CashPayoutLocationRequest, CreateCSPRequest, CreateCustomer, GetServiceChargeByCollection, Receiver, SearchCsp, SearchTransactionRequest, SendOtpRequest, SendTransasctionRequest, ValidateBankAccountRequest, ValidateTransactionRequest
from xml_request.services import client
from zeep.helpers import serialize_object
username = "testRps"
password = "testRps"
type_data = "IncomeSource"


# // RpsAdmin123
# // admin
class RequestMethods:
    @staticmethod
    def acpay_bank_branchlist(acPayBankListRequest:AcPayBankListRequest):
        response = client.service.AcPayBankBranchList(
               { 'UserName': username,
                'Password': password,
             **{k:v for k,v in  acPayBankListRequest.dict().items()}

                }
             )
        # Process the response 
        return serialize_object(response) 
    @staticmethod
    def cancel_transaction(cancelTransactionRequest:CancelTransactionRequest):
        response = client.service.CancelTransaction(
               { 
                'UserName': username,
                'Password': password,
                  **{k:v for k,v in  cancelTransactionRequest.dict().items()}

                }
             )
        # Process the response 
        return serialize_object(response) 
    
    @staticmethod
    def cash_payout_locationlist(cashPayoutLocationLost:CashPayoutLocationRequest):
        response = client.service.CashPayLocationList(
               { 
                'UserName': username,
                'Password': password,
                    **{k:v for k,v in  cashPayoutLocationLost.dict().items()}

                }
             )
        # Process the response 
        return serialize_object(response) 
    
    @staticmethod
    def create_csp(cspRequest:CreateCSPRequest):
        response = client.service.CreateCSPRequest(
               { 
                'UserName': username,
                'Password': password,
                'CSPCode': cspRequest,
                'EntityType':cspRequest,
                # 'OTPProcessId':opt_process_id,
                # 'OTP':otp

                }
             )
        # Process the response 
        return serialize_object(response) 
    @staticmethod
    def create_customers(customer:CreateCustomer):
        reqdata= { 
                'UserName': username,
                'Password': password,
                **{k:v for k,v in  customer.dict().items()}
    

                }
        print(reqdata)
        try:
            response = client.service.CreateCustomer(
                { 
                    'UserName': username,
                    'Password': password,
                    **{k:v for k,v in  customer.dict().items()}
        

                    }
                )
        except Exception as e:
            return e
        
        # print(data)
        # Process the response 
        return serialize_object(response) 
    
    @staticmethod
    def create_receivier(receiver:Receiver):
        response = client.service.CreateReceiver(
               { 
                'UserName': username,
                'Password': password,
                **{k:v for k,v in receiver.dict().items()}

                }
             )
        # Process the response 
        return serialize_object(response)  

    @staticmethod 
    def get_balance():
        response = client.service.GetBalance(
               { 
                'UserName': username,
                'Password': password,
                }
             )
        # Process the response 
        return serialize_object(response)  

    
    @staticmethod 
    def compliance_transactions():
        response = client.service.ComplianceTransactions (
               { 
                'UserName': username,
                'Password': password,
                
                }
             )
        # Process the response 
        return serialize_object(response) 
    
 

    @staticmethod
    def get_state_district(country:str):
        response = client.service.GetStateDistrict(
               { 'UserName': username,
                'Password': password,
                'Country': country}
             )
        # Process the response 
        return serialize_object(response) 
    @staticmethod
    def get_customer_by_id(id:int):
        response = client.service.GetCustomerByIdNumber(
               { 'UserName': username,
                'Password': password,
                'CustomerIdNo': id}
             )
        # Process the response 
        return serialize_object(response) 
    @staticmethod
    def get_cutomer_by_mobile(phone:str):
        response = client.service.GetCustomerByMobile(
               { 'UserName': username,
                'Password': password,
                'CustomerMobile': phone}
             )
        # Process the response 
        return serialize_object(response) 
    @staticmethod
    def get_static_data(type:str)->dict:
        # Call the 'GetStaticData' SOAP operation with the necessary parameters in the request body
        response = client.service.GetStaticData(
               { 'UserName': username,
                'Password': password,
                'Type': type}
             )
        # Process the response 
        return serialize_object(response) 
    @staticmethod
    def get_service_charge():
        response = client.service.GetServiceCharge(
             { 'UserName': username,
                'Password': password,
                'CollectionCurrency':'JPY',
                'Country':'Japan',
                'TransferAmount':'',
                'PayoutAmount':'',
                 }
        #     {
                # 'UserName': username,
                # 'Password': password,
                # 'Country':'',
                # 'TransferAmount':'',
                # 'PayoutAmount':'',
                # 'BranchId':''
                # 'IsNewAccount':''
            # }
        )
        print(response)
        return serialize_object(response) 
        # request=
 
    @staticmethod
    def get_service_charge_by_collection(serviceChageRequest:GetServiceChargeByCollection):
        response=client.service.GetServiceChargeByCollection({
            'UserName': username,
            'Password': password,
            **{k:v for k,v in serviceChageRequest.dict().items()}
            
            })
        return serialize_object(response) 
        
    @staticmethod
    def search_csp(searchRequest:SearchCsp):
        response=client.service.SearchCSP({
            'UserName': username,
            'Password': password,
            **{k:v for k,v in searchRequest.dict().items()}
            
            })
        return serialize_object(response) 
    
    @staticmethod
    def search_transaction(searchTransactionRequest:SearchTransactionRequest):
        response=client.service.SearchTransaction({
            'UserName': username,
            'Password': password,
            **{k:v for k,v in searchTransactionRequest.dict().items()}
            
            })
        return serialize_object(response) 

    @staticmethod
    def send_otp(otpRequest:SendOtpRequest):
        response=client.service.SendOTP({
            'UserName': username,
            'Password': password,
            **{k:v for k,v in otpRequest.dict().items()}
            
            })
        return serialize_object(response) 


    @staticmethod
    def send_transaction(sendTransactionRequest:SendTransasctionRequest):
        response=client.service.SendOTP({
            'UserName': username,
            'Password': password,
            **{k:v for k,v in sendTransactionRequest.dict().items()}
            
            })
        return serialize_object(response) 
    
    @staticmethod
    def unverified_customer():
        response=client.service.UnverifiedCustomers({
            'UserName': username,
            'Password': password,
            })
        return serialize_object(response) 
    
    @staticmethod
    def unverified_transactions():
        response=client.service.UnverifiedTransactions({
            'UserName': username,
            'Password': password,
            })
        return serialize_object(response) 
    
    @staticmethod
    def validate_bank_account(validateBankAccountRequest: ValidateBankAccountRequest):

        response=client.service.ValidateBankAccount({
                'UserName': username,
                'Password': password,
                **{k:v for k,v in validateBankAccountRequest.dict().items()}
                })
        return serialize_object(response) 
    
    @staticmethod
    def verifyTransactions(validateTransasctions:ValidateTransactionRequest):
        response=client.service.ValidateBankAccount({
                'UserName': username,
                'Password': password,
                **{k:v for k,v in validateTransasctions.dict().items()}
                })
        return serialize_object(response) 
    
    @staticmethod
    def upload_customer_document():
        # 
        
        response=client.service.UploadCustomerDocument({
                'UserName': username,
                'Password': password,
                **{k:v for k,v in validateTransasctions.dict().items()}
                })
        return serialize_object(response) 