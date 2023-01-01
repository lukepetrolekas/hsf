from tortoise import Model, fields

class ServiceType(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(128, null=False)
    simple = fields.CharField(128)

class Operator(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(256, null=False)
    phone = fields.CharField(20)
    address = fields.CharField(256)
    # total statement of all services
    gender = fields.IntField()
    sexpref = fields.BooleanField()
    Languages = fields.CharField(50)

class Service(Model):
    id = fields.IntField(pk=True)
    operator = fields.ForeignKeyField('models.Operator')
    service = fields.ForeignKeyField('models.ServiceType')
     # For this specific service offered
    gender = fields.IntField()
    sexpref = fields.IntField()
    minAge = fields.IntField()
    maxAge = fields.IntField()
    phone = fields.CharField(20)
    rrule = fields.CharField(1000)
    phone = fields.CharField(20)
    address = fields.CharField(256)
    citation = fields.CharField(500)
    lastUpdated = fields.DatetimeField(auto_now_add=True)