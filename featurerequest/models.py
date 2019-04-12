import datetime
from featurerequest import db
from sqlalchemy.dialects.mysql import ENUM

class FeatureRequest(db.Model):
    __tablename__ = 'feature_request'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    client = db.Column("client", ENUM("Client A", "Client B", "Client C", name="client_enum"), nullable=False)
    client_priority = db.Column(db.SmallInteger, nullable=False)
    target_date = db.Column(db.Date, nullable=False)
    product_area = db.Column("product_area", ENUM('Policies', 'Billing', 'Claims', 'Reports', name="product_area_enum"), nullable=False)
    created_at = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def save(self, commit=True):
        if commit:
            instance = self
            if not instance.id:
                db.session.add(instance)

            try:
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()
                return False

            return True
        return False

    def add(self):
        instance = self
        is_exist = instance.query.filter_by(client=instance.client).filter_by(
            client_priority=instance.client_priority).first()

        if not is_exist:
            return instance.save()

        for record in instance.query.filter_by(client=instance.client):
            record.client_priority += 1
            record.save()



        return instance.add()


