"""Add Payment and SecurityDeposit table  in database V2

Revision ID: 82240e029c4f
Revises: 503ca39def03
Create Date: 2023-04-22 12:39:36.006917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82240e029c4f'
down_revision = '503ca39def03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Apartment', schema=None) as batch_op:
        batch_op.alter_column('living_area',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=15, decimal_return_scale=4),
               existing_nullable=False)

    with op.batch_alter_table('Payment', schema=None) as batch_op:
        batch_op.alter_column('amount',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=15, decimal_return_scale=2),
               existing_nullable=False)

    with op.batch_alter_table('Price', schema=None) as batch_op:
        batch_op.alter_column('rent',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=15, decimal_return_scale=2),
               existing_nullable=False)
        batch_op.alter_column('charge',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=15, decimal_return_scale=2),
               existing_nullable=False)
        batch_op.alter_column('security_deposit',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=15, decimal_return_scale=2),
               existing_nullable=False)

    with op.batch_alter_table('Rental', schema=None) as batch_op:
        batch_op.alter_column('rental_balance',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=15, decimal_return_scale=2),
               existing_nullable=False)

    with op.batch_alter_table('Tenant', schema=None) as batch_op:
        batch_op.alter_column('annual_salary',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=15, decimal_return_scale=2),
               existing_nullable=False)
        batch_op.alter_column('balance',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=15, decimal_return_scale=2),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Tenant', schema=None) as batch_op:
        batch_op.alter_column('balance',
               existing_type=sa.Float(precision=15, decimal_return_scale=2),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('annual_salary',
               existing_type=sa.Float(precision=15, decimal_return_scale=2),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('Rental', schema=None) as batch_op:
        batch_op.alter_column('rental_balance',
               existing_type=sa.Float(precision=15, decimal_return_scale=2),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('Price', schema=None) as batch_op:
        batch_op.alter_column('security_deposit',
               existing_type=sa.Float(precision=15, decimal_return_scale=2),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.alter_column('charge',
               existing_type=sa.Float(precision=15, decimal_return_scale=2),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.alter_column('rent',
               existing_type=sa.Float(precision=15, decimal_return_scale=2),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('Payment', schema=None) as batch_op:
        batch_op.alter_column('amount',
               existing_type=sa.Float(precision=15, decimal_return_scale=2),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('Apartment', schema=None) as batch_op:
        batch_op.alter_column('living_area',
               existing_type=sa.Float(precision=15, decimal_return_scale=4),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###
