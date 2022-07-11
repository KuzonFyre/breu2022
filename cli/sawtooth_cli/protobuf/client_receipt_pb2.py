# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sawtooth_cli/protobuf/client_receipt.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sawtooth_cli.protobuf import transaction_receipt_pb2 as sawtooth__cli_dot_protobuf_dot_transaction__receipt__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sawtooth_cli/protobuf/client_receipt.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\n\025sawtooth.sdk.protobufP\001Z\022client_receipt_pb2'),
  serialized_pb=_b('\n*sawtooth_cli/protobuf/client_receipt.proto\x1a/sawtooth_cli/protobuf/transaction_receipt.proto\"2\n\x17\x43lientReceiptGetRequest\x12\x17\n\x0ftransaction_ids\x18\x01 \x03(\t\"\xcc\x01\n\x18\x43lientReceiptGetResponse\x12\x30\n\x06status\x18\x01 \x01(\x0e\x32 .ClientReceiptGetResponse.Status\x12%\n\x08receipts\x18\x02 \x03(\x0b\x32\x13.TransactionReceipt\"W\n\x06Status\x12\x10\n\x0cSTATUS_UNSET\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x12\n\x0eINTERNAL_ERROR\x10\x02\x12\x0f\n\x0bNO_RESOURCE\x10\x05\x12\x0e\n\nINVALID_ID\x10\x08\x42-\n\x15sawtooth.sdk.protobufP\x01Z\x12\x63lient_receipt_pb2b\x06proto3')
  ,
  dependencies=[sawtooth__cli_dot_protobuf_dot_transaction__receipt__pb2.DESCRIPTOR,])



_CLIENTRECEIPTGETRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='ClientReceiptGetResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_RESOURCE', index=3, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ID', index=4, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=265,
  serialized_end=352,
)
_sym_db.RegisterEnumDescriptor(_CLIENTRECEIPTGETRESPONSE_STATUS)


_CLIENTRECEIPTGETREQUEST = _descriptor.Descriptor(
  name='ClientReceiptGetRequest',
  full_name='ClientReceiptGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction_ids', full_name='ClientReceiptGetRequest.transaction_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=145,
)


_CLIENTRECEIPTGETRESPONSE = _descriptor.Descriptor(
  name='ClientReceiptGetResponse',
  full_name='ClientReceiptGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ClientReceiptGetResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receipts', full_name='ClientReceiptGetResponse.receipts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CLIENTRECEIPTGETRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=352,
)

_CLIENTRECEIPTGETRESPONSE.fields_by_name['status'].enum_type = _CLIENTRECEIPTGETRESPONSE_STATUS
_CLIENTRECEIPTGETRESPONSE.fields_by_name['receipts'].message_type = sawtooth__cli_dot_protobuf_dot_transaction__receipt__pb2._TRANSACTIONRECEIPT
_CLIENTRECEIPTGETRESPONSE_STATUS.containing_type = _CLIENTRECEIPTGETRESPONSE
DESCRIPTOR.message_types_by_name['ClientReceiptGetRequest'] = _CLIENTRECEIPTGETREQUEST
DESCRIPTOR.message_types_by_name['ClientReceiptGetResponse'] = _CLIENTRECEIPTGETRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientReceiptGetRequest = _reflection.GeneratedProtocolMessageType('ClientReceiptGetRequest', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTRECEIPTGETREQUEST,
  __module__ = 'sawtooth_cli.protobuf.client_receipt_pb2'
  # @@protoc_insertion_point(class_scope:ClientReceiptGetRequest)
  ))
_sym_db.RegisterMessage(ClientReceiptGetRequest)

ClientReceiptGetResponse = _reflection.GeneratedProtocolMessageType('ClientReceiptGetResponse', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTRECEIPTGETRESPONSE,
  __module__ = 'sawtooth_cli.protobuf.client_receipt_pb2'
  # @@protoc_insertion_point(class_scope:ClientReceiptGetResponse)
  ))
_sym_db.RegisterMessage(ClientReceiptGetResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
