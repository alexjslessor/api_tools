
from pydantic import BaseModel
import bson
import datetime


datetime_to_unix_epoch = lambda x: x.timestamp()

class BaseConfig(BaseModel):

    def to_dict(self, **kwargs):
        data = self.dict(by_alias=True)
        data["_id"] = str(self.id)
        return data

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            datetime.datetime: datetime_to_unix_epoch,
            bson.decimal128.Decimal128: lambda x: str(x),
            bson.ObjectId: str
        }
