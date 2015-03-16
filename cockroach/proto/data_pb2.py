# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cockroach/proto/data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import cockroach.proto.config_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cockroach/proto/data.proto',
  package='cockroach.proto',
  serialized_pb=_b('\n\x1a\x63ockroach/proto/data.proto\x12\x0f\x63ockroach.proto\x1a\x1c\x63ockroach/proto/config.proto\"/\n\tTimestamp\x12\x11\n\twall_time\x18\x01 \x01(\x03\x12\x0f\n\x07logical\x18\x02 \x01(\x05\"u\n\x05Value\x12\r\n\x05\x62ytes\x18\x01 \x01(\x0c\x12\x0f\n\x07integer\x18\x02 \x01(\x03\x12\x10\n\x08\x63hecksum\x18\x03 \x01(\x07\x12-\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.cockroach.proto.Timestamp\x12\x0b\n\x03tag\x18\x05 \x01(\t\"C\n\tMVCCValue\x12\x0f\n\x07\x64\x65leted\x18\x01 \x01(\x08\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.cockroach.proto.Value\">\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.cockroach.proto.Value\")\n\x0bRawKeyValue\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\"C\n\nStoreIdent\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x0f\n\x07node_id\x18\x02 \x01(\x05\x12\x10\n\x08store_id\x18\x03 \x01(\x05\"z\n\x0cSplitTrigger\x12\x36\n\x0cupdated_desc\x18\x01 \x01(\x0b\x32 .cockroach.proto.RangeDescriptor\x12\x32\n\x08new_desc\x18\x02 \x01(\x0b\x32 .cockroach.proto.RangeDescriptor\"`\n\x0cMergeTrigger\x12\x36\n\x0cupdated_desc\x18\x01 \x01(\x0b\x32 .cockroach.proto.RangeDescriptor\x12\x18\n\x10subsumed_raft_id\x18\x02 \x01(\x03\"\xa7\x01\n\x15\x43hangeReplicasTrigger\x12\x0f\n\x07node_id\x18\x01 \x01(\x05\x12\x10\n\x08store_id\x18\x02 \x01(\x05\x12\x37\n\x0b\x63hange_type\x18\x03 \x01(\x0e\x32\".cockroach.proto.ReplicaChangeType\x12\x32\n\x10updated_replicas\x18\x04 \x03(\x0b\x32\x18.cockroach.proto.Replica\"\xcc\x01\n\x15InternalCommitTrigger\x12\x34\n\rsplit_trigger\x18\x01 \x01(\x0b\x32\x1d.cockroach.proto.SplitTrigger\x12\x34\n\rmerge_trigger\x18\x02 \x01(\x0b\x32\x1d.cockroach.proto.MergeTrigger\x12G\n\x17\x63hange_replicas_trigger\x18\x03 \x01(\x0b\x32&.cockroach.proto.ChangeReplicasTrigger\"\x1d\n\x08NodeList\x12\x11\n\x05nodes\x18\x01 \x03(\x05\x42\x02\x10\x01\"\xb8\x03\n\x0bTransaction\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12\n\n\x02id\x18\x03 \x01(\x0c\x12\x10\n\x08priority\x18\x04 \x01(\x05\x12\x31\n\tisolation\x18\x05 \x01(\x0e\x32\x1e.cockroach.proto.IsolationType\x12\x32\n\x06status\x18\x06 \x01(\x0e\x32\".cockroach.proto.TransactionStatus\x12\r\n\x05\x65poch\x18\x07 \x01(\x05\x12\x32\n\x0elast_heartbeat\x18\x08 \x01(\x0b\x32\x1a.cockroach.proto.Timestamp\x12-\n\ttimestamp\x18\t \x01(\x0b\x32\x1a.cockroach.proto.Timestamp\x12\x32\n\x0eorig_timestamp\x18\n \x01(\x0b\x32\x1a.cockroach.proto.Timestamp\x12\x31\n\rmax_timestamp\x18\x0b \x01(\x0b\x32\x1a.cockroach.proto.Timestamp\x12\x30\n\rcertain_nodes\x18\x0c \x01(\x0b\x32\x19.cockroach.proto.NodeList\"\xc6\x01\n\x0cMVCCMetadata\x12)\n\x03txn\x18\x01 \x01(\x0b\x32\x1c.cockroach.proto.Transaction\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.cockroach.proto.Timestamp\x12\x0f\n\x07\x64\x65leted\x18\x03 \x01(\x08\x12\x11\n\tkey_bytes\x18\x04 \x01(\x03\x12\x11\n\tval_bytes\x18\x05 \x01(\x03\x12%\n\x05value\x18\x06 \x01(\x0b\x32\x16.cockroach.proto.Value\"B\n\nGCMetadata\x12\x17\n\x0flast_scan_nanos\x18\x01 \x01(\x03\x12\x1b\n\x13oldest_intent_nanos\x18\x02 \x01(\x03\"V\n\x13TimeSeriesDatapoint\x12\x17\n\x0ftimestamp_nanos\x18\x01 \x01(\x03\x12\x11\n\tint_value\x18\x02 \x01(\x03\x12\x13\n\x0b\x66loat_value\x18\x03 \x01(\x02\"X\n\x0eTimeSeriesData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x38\n\ndatapoints\x18\x02 \x03(\x0b\x32$.cockroach.proto.TimeSeriesDatapoint*8\n\x11ReplicaChangeType\x12\x0f\n\x0b\x41\x44\x44_REPLICA\x10\x00\x12\x12\n\x0eREMOVE_REPLICA\x10\x01*/\n\rIsolationType\x12\x10\n\x0cSERIALIZABLE\x10\x00\x12\x0c\n\x08SNAPSHOT\x10\x01*<\n\x11TransactionStatus\x12\x0b\n\x07PENDING\x10\x00\x12\r\n\tCOMMITTED\x10\x01\x12\x0b\n\x07\x41\x42ORTED\x10\x02\x42\x07Z\x05proto')
  ,
  dependencies=[cockroach.proto.config_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_REPLICACHANGETYPE = _descriptor.EnumDescriptor(
  name='ReplicaChangeType',
  full_name='cockroach.proto.ReplicaChangeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADD_REPLICA', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE_REPLICA', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2010,
  serialized_end=2066,
)
_sym_db.RegisterEnumDescriptor(_REPLICACHANGETYPE)

ReplicaChangeType = enum_type_wrapper.EnumTypeWrapper(_REPLICACHANGETYPE)
_ISOLATIONTYPE = _descriptor.EnumDescriptor(
  name='IsolationType',
  full_name='cockroach.proto.IsolationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SERIALIZABLE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SNAPSHOT', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2068,
  serialized_end=2115,
)
_sym_db.RegisterEnumDescriptor(_ISOLATIONTYPE)

IsolationType = enum_type_wrapper.EnumTypeWrapper(_ISOLATIONTYPE)
_TRANSACTIONSTATUS = _descriptor.EnumDescriptor(
  name='TransactionStatus',
  full_name='cockroach.proto.TransactionStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMITTED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ABORTED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2117,
  serialized_end=2177,
)
_sym_db.RegisterEnumDescriptor(_TRANSACTIONSTATUS)

TransactionStatus = enum_type_wrapper.EnumTypeWrapper(_TRANSACTIONSTATUS)
ADD_REPLICA = 0
REMOVE_REPLICA = 1
SERIALIZABLE = 0
SNAPSHOT = 1
PENDING = 0
COMMITTED = 1
ABORTED = 2



_TIMESTAMP = _descriptor.Descriptor(
  name='Timestamp',
  full_name='cockroach.proto.Timestamp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wall_time', full_name='cockroach.proto.Timestamp.wall_time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='logical', full_name='cockroach.proto.Timestamp.logical', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=124,
)


_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='cockroach.proto.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bytes', full_name='cockroach.proto.Value.bytes', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='integer', full_name='cockroach.proto.Value.integer', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='checksum', full_name='cockroach.proto.Value.checksum', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='cockroach.proto.Value.timestamp', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag', full_name='cockroach.proto.Value.tag', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=243,
)


_MVCCVALUE = _descriptor.Descriptor(
  name='MVCCValue',
  full_name='cockroach.proto.MVCCValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deleted', full_name='cockroach.proto.MVCCValue.deleted', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='cockroach.proto.MVCCValue.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=245,
  serialized_end=312,
)


_KEYVALUE = _descriptor.Descriptor(
  name='KeyValue',
  full_name='cockroach.proto.KeyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='cockroach.proto.KeyValue.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='cockroach.proto.KeyValue.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=314,
  serialized_end=376,
)


_RAWKEYVALUE = _descriptor.Descriptor(
  name='RawKeyValue',
  full_name='cockroach.proto.RawKeyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='cockroach.proto.RawKeyValue.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='cockroach.proto.RawKeyValue.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=378,
  serialized_end=419,
)


_STOREIDENT = _descriptor.Descriptor(
  name='StoreIdent',
  full_name='cockroach.proto.StoreIdent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='cockroach.proto.StoreIdent.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='cockroach.proto.StoreIdent.node_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='store_id', full_name='cockroach.proto.StoreIdent.store_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=421,
  serialized_end=488,
)


_SPLITTRIGGER = _descriptor.Descriptor(
  name='SplitTrigger',
  full_name='cockroach.proto.SplitTrigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='updated_desc', full_name='cockroach.proto.SplitTrigger.updated_desc', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_desc', full_name='cockroach.proto.SplitTrigger.new_desc', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=490,
  serialized_end=612,
)


_MERGETRIGGER = _descriptor.Descriptor(
  name='MergeTrigger',
  full_name='cockroach.proto.MergeTrigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='updated_desc', full_name='cockroach.proto.MergeTrigger.updated_desc', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subsumed_raft_id', full_name='cockroach.proto.MergeTrigger.subsumed_raft_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=614,
  serialized_end=710,
)


_CHANGEREPLICASTRIGGER = _descriptor.Descriptor(
  name='ChangeReplicasTrigger',
  full_name='cockroach.proto.ChangeReplicasTrigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_id', full_name='cockroach.proto.ChangeReplicasTrigger.node_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='store_id', full_name='cockroach.proto.ChangeReplicasTrigger.store_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='change_type', full_name='cockroach.proto.ChangeReplicasTrigger.change_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updated_replicas', full_name='cockroach.proto.ChangeReplicasTrigger.updated_replicas', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=713,
  serialized_end=880,
)


_INTERNALCOMMITTRIGGER = _descriptor.Descriptor(
  name='InternalCommitTrigger',
  full_name='cockroach.proto.InternalCommitTrigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='split_trigger', full_name='cockroach.proto.InternalCommitTrigger.split_trigger', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='merge_trigger', full_name='cockroach.proto.InternalCommitTrigger.merge_trigger', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='change_replicas_trigger', full_name='cockroach.proto.InternalCommitTrigger.change_replicas_trigger', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=883,
  serialized_end=1087,
)


_NODELIST = _descriptor.Descriptor(
  name='NodeList',
  full_name='cockroach.proto.NodeList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='cockroach.proto.NodeList.nodes', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1089,
  serialized_end=1118,
)


_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='cockroach.proto.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cockroach.proto.Transaction.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='cockroach.proto.Transaction.key', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='cockroach.proto.Transaction.id', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='priority', full_name='cockroach.proto.Transaction.priority', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isolation', full_name='cockroach.proto.Transaction.isolation', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='cockroach.proto.Transaction.status', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='epoch', full_name='cockroach.proto.Transaction.epoch', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_heartbeat', full_name='cockroach.proto.Transaction.last_heartbeat', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='cockroach.proto.Transaction.timestamp', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orig_timestamp', full_name='cockroach.proto.Transaction.orig_timestamp', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_timestamp', full_name='cockroach.proto.Transaction.max_timestamp', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='certain_nodes', full_name='cockroach.proto.Transaction.certain_nodes', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1121,
  serialized_end=1561,
)


_MVCCMETADATA = _descriptor.Descriptor(
  name='MVCCMetadata',
  full_name='cockroach.proto.MVCCMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txn', full_name='cockroach.proto.MVCCMetadata.txn', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='cockroach.proto.MVCCMetadata.timestamp', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deleted', full_name='cockroach.proto.MVCCMetadata.deleted', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key_bytes', full_name='cockroach.proto.MVCCMetadata.key_bytes', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='val_bytes', full_name='cockroach.proto.MVCCMetadata.val_bytes', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='cockroach.proto.MVCCMetadata.value', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1564,
  serialized_end=1762,
)


_GCMETADATA = _descriptor.Descriptor(
  name='GCMetadata',
  full_name='cockroach.proto.GCMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='last_scan_nanos', full_name='cockroach.proto.GCMetadata.last_scan_nanos', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='oldest_intent_nanos', full_name='cockroach.proto.GCMetadata.oldest_intent_nanos', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1764,
  serialized_end=1830,
)


_TIMESERIESDATAPOINT = _descriptor.Descriptor(
  name='TimeSeriesDatapoint',
  full_name='cockroach.proto.TimeSeriesDatapoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp_nanos', full_name='cockroach.proto.TimeSeriesDatapoint.timestamp_nanos', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int_value', full_name='cockroach.proto.TimeSeriesDatapoint.int_value', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='float_value', full_name='cockroach.proto.TimeSeriesDatapoint.float_value', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1832,
  serialized_end=1918,
)


_TIMESERIESDATA = _descriptor.Descriptor(
  name='TimeSeriesData',
  full_name='cockroach.proto.TimeSeriesData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cockroach.proto.TimeSeriesData.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datapoints', full_name='cockroach.proto.TimeSeriesData.datapoints', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1920,
  serialized_end=2008,
)

_VALUE.fields_by_name['timestamp'].message_type = _TIMESTAMP
_MVCCVALUE.fields_by_name['value'].message_type = _VALUE
_KEYVALUE.fields_by_name['value'].message_type = _VALUE
_SPLITTRIGGER.fields_by_name['updated_desc'].message_type = cockroach.proto.config_pb2._RANGEDESCRIPTOR
_SPLITTRIGGER.fields_by_name['new_desc'].message_type = cockroach.proto.config_pb2._RANGEDESCRIPTOR
_MERGETRIGGER.fields_by_name['updated_desc'].message_type = cockroach.proto.config_pb2._RANGEDESCRIPTOR
_CHANGEREPLICASTRIGGER.fields_by_name['change_type'].enum_type = _REPLICACHANGETYPE
_CHANGEREPLICASTRIGGER.fields_by_name['updated_replicas'].message_type = cockroach.proto.config_pb2._REPLICA
_INTERNALCOMMITTRIGGER.fields_by_name['split_trigger'].message_type = _SPLITTRIGGER
_INTERNALCOMMITTRIGGER.fields_by_name['merge_trigger'].message_type = _MERGETRIGGER
_INTERNALCOMMITTRIGGER.fields_by_name['change_replicas_trigger'].message_type = _CHANGEREPLICASTRIGGER
_TRANSACTION.fields_by_name['isolation'].enum_type = _ISOLATIONTYPE
_TRANSACTION.fields_by_name['status'].enum_type = _TRANSACTIONSTATUS
_TRANSACTION.fields_by_name['last_heartbeat'].message_type = _TIMESTAMP
_TRANSACTION.fields_by_name['timestamp'].message_type = _TIMESTAMP
_TRANSACTION.fields_by_name['orig_timestamp'].message_type = _TIMESTAMP
_TRANSACTION.fields_by_name['max_timestamp'].message_type = _TIMESTAMP
_TRANSACTION.fields_by_name['certain_nodes'].message_type = _NODELIST
_MVCCMETADATA.fields_by_name['txn'].message_type = _TRANSACTION
_MVCCMETADATA.fields_by_name['timestamp'].message_type = _TIMESTAMP
_MVCCMETADATA.fields_by_name['value'].message_type = _VALUE
_TIMESERIESDATA.fields_by_name['datapoints'].message_type = _TIMESERIESDATAPOINT
DESCRIPTOR.message_types_by_name['Timestamp'] = _TIMESTAMP
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['MVCCValue'] = _MVCCVALUE
DESCRIPTOR.message_types_by_name['KeyValue'] = _KEYVALUE
DESCRIPTOR.message_types_by_name['RawKeyValue'] = _RAWKEYVALUE
DESCRIPTOR.message_types_by_name['StoreIdent'] = _STOREIDENT
DESCRIPTOR.message_types_by_name['SplitTrigger'] = _SPLITTRIGGER
DESCRIPTOR.message_types_by_name['MergeTrigger'] = _MERGETRIGGER
DESCRIPTOR.message_types_by_name['ChangeReplicasTrigger'] = _CHANGEREPLICASTRIGGER
DESCRIPTOR.message_types_by_name['InternalCommitTrigger'] = _INTERNALCOMMITTRIGGER
DESCRIPTOR.message_types_by_name['NodeList'] = _NODELIST
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.message_types_by_name['MVCCMetadata'] = _MVCCMETADATA
DESCRIPTOR.message_types_by_name['GCMetadata'] = _GCMETADATA
DESCRIPTOR.message_types_by_name['TimeSeriesDatapoint'] = _TIMESERIESDATAPOINT
DESCRIPTOR.message_types_by_name['TimeSeriesData'] = _TIMESERIESDATA
DESCRIPTOR.enum_types_by_name['ReplicaChangeType'] = _REPLICACHANGETYPE
DESCRIPTOR.enum_types_by_name['IsolationType'] = _ISOLATIONTYPE
DESCRIPTOR.enum_types_by_name['TransactionStatus'] = _TRANSACTIONSTATUS

Timestamp = _reflection.GeneratedProtocolMessageType('Timestamp', (_message.Message,), dict(
  DESCRIPTOR = _TIMESTAMP,
  __module__ = 'cockroach.proto.data_pb2'
  # @@protoc_insertion_point(class_scope:cockroach.proto.Timestamp)
  ))
_sym_db.RegisterMessage(Timestamp)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), dict(
  DESCRIPTOR = _VALUE,
  __module__ = 'cockroach.proto.data_pb2'
  # @@protoc_insertion_point(class_scope:cockroach.proto.Value)
  ))
_sym_db.RegisterMessage(Value)

MVCCValue = _reflection.GeneratedProtocolMessageType('MVCCValue', (_message.Message,), dict(
  DESCRIPTOR = _MVCCVALUE,
  __module__ = 'cockroach.proto.data_pb2'
  # @@protoc_insertion_point(class_scope:cockroach.proto.MVCCValue)
  ))
_sym_db.RegisterMessage(MVCCValue)

KeyValue = _reflection.GeneratedProtocolMessageType('KeyValue', (_message.Message,), dict(
  DESCRIPTOR = _KEYVALUE,
  __module__ = 'cockroach.proto.data_pb2'
  # @@protoc_insertion_point(class_scope:cockroach.proto.KeyValue)
  ))
_sym_db.RegisterMessage(KeyValue)

RawKeyValue = _reflection.GeneratedProtocolMessageType('RawKeyValue', (_message.Message,), dict(
  DESCRIPTOR = _RAWKEYVALUE,
  __module__ = 'cockroach.proto.data_pb2'
  # @@protoc_insertion_point(class_scope:cockroach.proto.RawKeyValue)
  ))
_sym_db.RegisterMessage(RawKeyValue)

StoreIdent = _reflection.GeneratedProtocolMessageType('StoreIdent', (_message.Message,), dict(
  DESCRIPTOR = _STOREIDENT,
  __module__ = 'cockroach.proto.data_pb2'
  # @@protoc_insertion_point(class_scope:cockroach.proto.StoreIdent)
  ))
_sym_db.RegisterMessage(StoreIdent)

SplitTrigger = _reflection.GeneratedProtocolMessageType('SplitTrigger', (_message.Message,), dict(
  DESCRIPTOR = _SPLITTRIGGER,
  __module__ = 'cockroach.proto.data_pb2'
  # @@protoc_insertion_point(class_scope:cockroach.proto.SplitTrigger)
  ))
_sym_db.RegisterMessage(SplitTrigger)

MergeTrigger = _reflection.GeneratedProtocolMessageType('MergeTrigger', (_message.Message,), dict(
  DESCRIPTOR = _MERGETRIGGER,
  __module__ = 'cockroach.proto.data_pb2'
  # @@protoc_insertion_point(class_scope:cockroach.proto.MergeTrigger)
  ))
_sym_db.RegisterMessage(MergeTrigger)

ChangeReplicasTrigger = _reflection.GeneratedProtocolMessageType('ChangeReplicasTrigger', (_message.Message,), dict(
  DESCRIPTOR = _CHANGEREPLICASTRIGGER,
  __module__ = 'cockroach.proto.data_pb2'
  # @@protoc_insertion_point(class_scope:cockroach.proto.ChangeReplicasTrigger)
  ))
_sym_db.RegisterMessage(ChangeReplicasTrigger)

InternalCommitTrigger = _reflection.GeneratedProtocolMessageType('InternalCommitTrigger', (_message.Message,), dict(
  DESCRIPTOR = _INTERNALCOMMITTRIGGER,
  __module__ = 'cockroach.proto.data_pb2'
  # @@protoc_insertion_point(class_scope:cockroach.proto.InternalCommitTrigger)
  ))
_sym_db.RegisterMessage(InternalCommitTrigger)

NodeList = _reflection.GeneratedProtocolMessageType('NodeList', (_message.Message,), dict(
  DESCRIPTOR = _NODELIST,
  __module__ = 'cockroach.proto.data_pb2'
  # @@protoc_insertion_point(class_scope:cockroach.proto.NodeList)
  ))
_sym_db.RegisterMessage(NodeList)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTION,
  __module__ = 'cockroach.proto.data_pb2'
  # @@protoc_insertion_point(class_scope:cockroach.proto.Transaction)
  ))
_sym_db.RegisterMessage(Transaction)

MVCCMetadata = _reflection.GeneratedProtocolMessageType('MVCCMetadata', (_message.Message,), dict(
  DESCRIPTOR = _MVCCMETADATA,
  __module__ = 'cockroach.proto.data_pb2'
  # @@protoc_insertion_point(class_scope:cockroach.proto.MVCCMetadata)
  ))
_sym_db.RegisterMessage(MVCCMetadata)

GCMetadata = _reflection.GeneratedProtocolMessageType('GCMetadata', (_message.Message,), dict(
  DESCRIPTOR = _GCMETADATA,
  __module__ = 'cockroach.proto.data_pb2'
  # @@protoc_insertion_point(class_scope:cockroach.proto.GCMetadata)
  ))
_sym_db.RegisterMessage(GCMetadata)

TimeSeriesDatapoint = _reflection.GeneratedProtocolMessageType('TimeSeriesDatapoint', (_message.Message,), dict(
  DESCRIPTOR = _TIMESERIESDATAPOINT,
  __module__ = 'cockroach.proto.data_pb2'
  # @@protoc_insertion_point(class_scope:cockroach.proto.TimeSeriesDatapoint)
  ))
_sym_db.RegisterMessage(TimeSeriesDatapoint)

TimeSeriesData = _reflection.GeneratedProtocolMessageType('TimeSeriesData', (_message.Message,), dict(
  DESCRIPTOR = _TIMESERIESDATA,
  __module__ = 'cockroach.proto.data_pb2'
  # @@protoc_insertion_point(class_scope:cockroach.proto.TimeSeriesData)
  ))
_sym_db.RegisterMessage(TimeSeriesData)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\005proto'))
_NODELIST.fields_by_name['nodes'].has_options = True
_NODELIST.fields_by_name['nodes']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
