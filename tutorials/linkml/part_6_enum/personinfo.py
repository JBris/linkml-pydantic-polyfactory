# Auto generated from personinfo-mapped.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-07-13T23:21:00
# Schema: personinfo
#
# id: https://w3id.org/linkml/examples/personinfo
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"
version = None

# Namespaces
ORCID = CurieNamespace('ORCID', 'https://orcid.org/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PERSONINFO = CurieNamespace('personinfo', 'https://w3id.org/linkml/examples/personinfo/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = PERSONINFO


# Types

# Class references
class PersonId(extended_str):
    pass


@dataclass(repr=False)
class Person(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Person"]
    class_class_curie: ClassVar[str] = "schema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = PERSONINFO.Person

    id: Union[str, PersonId] = None
    full_name: str = None
    aliases: Optional[Union[str, list[str]]] = empty_list()
    phone: Optional[str] = None
    age: Optional[int] = None
    status: Optional[Union[str, "PersonStatus"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self._is_empty(self.full_name):
            self.MissingRequiredField("full_name")
        if not isinstance(self.full_name, str):
            self.full_name = str(self.full_name)

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        if self.phone is not None and not isinstance(self.phone, str):
            self.phone = str(self.phone)

        if self.age is not None and not isinstance(self.age, int):
            self.age = int(self.age)

        if self.status is not None and not isinstance(self.status, PersonStatus):
            self.status = PersonStatus(self.status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Container(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PERSONINFO["Container"]
    class_class_curie: ClassVar[str] = "personinfo:Container"
    class_name: ClassVar[str] = "Container"
    class_model_uri: ClassVar[URIRef] = PERSONINFO.Container

    persons: Optional[Union[dict[Union[str, PersonId], Union[dict, Person]], list[Union[dict, Person]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="persons", slot_type=Person, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class PersonStatus(EnumDefinitionImpl):

    ALIVE = PermissibleValue(
        text="ALIVE",
        description="the person is living",
        meaning=PATO["0001421"])
    DEAD = PermissibleValue(
        text="DEAD",
        description="the person is deceased",
        meaning=PATO["0001422"])
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="the vital status is not known")

    _defn = EnumDefinition(
        name="PersonStatus",
    )

# Slots
class slots:
    pass

slots.person__id = Slot(uri=PERSONINFO.id, name="person__id", curie=PERSONINFO.curie('id'),
                   model_uri=PERSONINFO.person__id, domain=None, range=URIRef)

slots.person__full_name = Slot(uri=SCHEMA.name, name="person__full_name", curie=SCHEMA.curie('name'),
                   model_uri=PERSONINFO.person__full_name, domain=None, range=str)

slots.person__aliases = Slot(uri=PERSONINFO.aliases, name="person__aliases", curie=PERSONINFO.curie('aliases'),
                   model_uri=PERSONINFO.person__aliases, domain=None, range=Optional[Union[str, list[str]]])

slots.person__phone = Slot(uri=SCHEMA.telephone, name="person__phone", curie=SCHEMA.curie('telephone'),
                   model_uri=PERSONINFO.person__phone, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\d\(\)\-]+$'))

slots.person__age = Slot(uri=PERSONINFO.age, name="person__age", curie=PERSONINFO.curie('age'),
                   model_uri=PERSONINFO.person__age, domain=None, range=Optional[int])

slots.person__status = Slot(uri=PERSONINFO.status, name="person__status", curie=PERSONINFO.curie('status'),
                   model_uri=PERSONINFO.person__status, domain=None, range=Optional[Union[str, "PersonStatus"]])

slots.container__persons = Slot(uri=PERSONINFO.persons, name="container__persons", curie=PERSONINFO.curie('persons'),
                   model_uri=PERSONINFO.container__persons, domain=None, range=Optional[Union[dict[Union[str, PersonId], Union[dict, Person]], list[Union[dict, Person]]]])
