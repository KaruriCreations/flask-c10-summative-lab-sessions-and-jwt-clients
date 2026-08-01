from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=3))
    password = fields.Str(load_only=True, required=True, validate=validate.Length(min=4))

class NoteSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=1))
    content = fields.Str(required=True)
    user_id = fields.Int(dump_only=True)