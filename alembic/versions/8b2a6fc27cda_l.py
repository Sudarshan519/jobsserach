"""l

Revision ID: 8b2a6fc27cda
Revises: 
Create Date: 2023-07-29 00:49:42.912927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b2a6fc27cda'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'leaverequest', 'companymodel', ['company_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'leaverequest', type_='foreignkey')
    # ### end Alembic commands ###