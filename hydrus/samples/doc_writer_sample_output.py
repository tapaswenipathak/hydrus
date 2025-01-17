"""Generated API Documentation sample using doc_writer_sample.py."""
    
doc = {
    "@context": {
        "ApiDocumentation": "hydra:ApiDocumentation",
        "description": "hydra:description",
        "domain": {
            "@id": "rdfs:domain",
            "@type": "@id"
        },
        "expects": {
            "@id": "hydra:expects",
            "@type": "@id"
        },
        "hydra": "http://www.w3.org/ns/hydra/core#",
        "label": "rdfs:label",
        "method": "hydra:method",
        "possibleStatus": "hydra:possibleStatus",
        "property": {
            "@id": "hydra:property",
            "@type": "@id"
        },
        "range": {
            "@id": "rdfs:range",
            "@type": "@id"
        },
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "readonly": "hydra:readonly",
        "required": "hydra:required",
        "returns": {
            "@id": "hydra:returns",
            "@type": "@id"
        },
        "statusCode": "hydra:statusCode",
        "subClassOf": {
            "@id": "rdfs:subClassOf",
            "@type": "@id"
        },
        "supportedClass": "hydra:supportedClass",
        "supportedOperation": "hydra:supportedOperation",
        "supportedProperty": "hydra:supportedProperty",
        "title": "hydra:title",
        "vocab": "https://hydrus.com/api/vocab#",
        "writeonly": "hydra:writeonly"
    },
    "@id": "https://hydrus.com/api/vocab",
    "@type": "ApiDocumentation",
    "description": "Description for the API Documentation",
    "possibleStatus": [],
    "supportedClass": [
        {
            "@id": "vocab:singleClass",
            "@type": "hydra:Class",
            "description": "A non collection class",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "vocab:singleClass",
                    "method": "POST",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "",
                            "statusCode": 200,
                            "title": "singleClass changed."
                        }
                    ],
                    "returns": "null",
                    "title": "UpdateClass"
                },
                {
                    "@type": "http://schema.org/DeleteAction",
                    "expects": "null",
                    "method": "DELETE",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "",
                            "statusCode": 200,
                            "title": "singleClass deleted."
                        }
                    ],
                    "returns": "null",
                    "title": "DeleteClass"
                },
                {
                    "@type": "http://schema.org/AddAction",
                    "expects": "vocab:singleClass",
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "",
                            "statusCode": 201,
                            "title": "singleClass successfully added."
                        }
                    ],
                    "returns": "null",
                    "title": "AddClass"
                },
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "null",
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "",
                            "statusCode": 200,
                            "title": "singleClass returned."
                        }
                    ],
                    "returns": "vocab:singleClass",
                    "title": "GetClass"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://props.hydrus.com/prop1",
                    "readonly": "false",
                    "required": "true",
                    "title": "Prop1",
                    "writeonly": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://props.hydrus.com/prop1",
                    "readonly": "false",
                    "required": "false",
                    "title": "Prop2",
                    "writeonly": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:dummyClass",
                    "readonly": "false",
                    "required": "false",
                    "title": "dummyProp",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:anotherSingleClass",
                    "readonly": "false",
                    "required": "false",
                    "title": "singleClassProp",
                    "writeonly": "false"
                }
            ],
            "title": "singleClass"
        },
        {
            "@id": "vocab:anotherSingleClass",
            "@type": "hydra:Class",
            "description": "An another non collection class",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "null",
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "",
                            "statusCode": 200,
                            "title": "anotherSingleClass returned."
                        }
                    ],
                    "returns": "vocab:anotherSingleClass",
                    "title": "GetClass"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://props.hydrus.com/prop1",
                    "readonly": "false",
                    "required": "true",
                    "title": "Prop1",
                    "writeonly": "true"
                }
            ],
            "title": "anotherSingleClass"
        },
        {
            "@id": "vocab:extraClass",
            "@type": "hydra:Class",
            "description": "Class without any explicit methods",
            "supportedOperation": [],
            "supportedProperty": [],
            "title": "extraClass"
        },
        {
            "@id": "vocab:dummyClass",
            "@type": "hydra:Class",
            "description": "A dummyClass for demo",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "vocab:dummyClass",
                    "method": "POST",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "",
                            "statusCode": 200,
                            "title": "dummyClass updated."
                        }
                    ],
                    "returns": "null",
                    "title": "UpdateClass"
                },
                {
                    "@type": "http://schema.org/DeleteAction",
                    "expects": "null",
                    "method": "DELETE",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "",
                            "statusCode": 200,
                            "title": "dummyClass deleted."
                        }
                    ],
                    "returns": "null",
                    "title": "DeleteClass"
                },
                {
                    "@type": "http://schema.org/AddAction",
                    "expects": "vocab:dummyClass",
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "",
                            "statusCode": 201,
                            "title": "dummyClass successfully added."
                        }
                    ],
                    "returns": "null",
                    "title": "AddClass"
                },
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "null",
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "",
                            "statusCode": 200,
                            "title": "dummyClass returned."
                        }
                    ],
                    "returns": "vocab:dummyClass",
                    "title": "GetClass"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://props.hydrus.com/prop1",
                    "readonly": "false",
                    "required": "true",
                    "title": "Prop1",
                    "writeonly": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://props.hydrus.com/prop1",
                    "readonly": "false",
                    "required": "false",
                    "title": "Prop2",
                    "writeonly": "true"
                }
            ],
            "title": "dummyClass"
        },
        {
            "@id": "http://www.w3.org/ns/hydra/core#Resource",
            "@type": "hydra:Class",
            "description": "null",
            "supportedOperation": [],
            "supportedProperty": [],
            "title": "Resource"
        },
        {
            "@id": "http://www.w3.org/ns/hydra/core#Collection",
            "@type": "hydra:Class",
            "description": "null",
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "required": "null",
                    "title": "members",
                    "writeonly": "false"
                }
            ],
            "title": "Collection"
        },
        {
            "@id": "vocab:dummyClassCollection",
            "@type": "hydra:Class",
            "description": "A collection of dummyclass",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:dummyclass_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all dummyClass entities",
                    "expects": "null",
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:dummyClassCollection"
                },
                {
                    "@id": "_:dummyclass_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new dummyClass entity",
                    "expects": "vocab:dummyClass",
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "If the dummyClass entity was createdsuccessfully.",
                            "statusCode": 201,
                            "title": ""
                        }
                    ],
                    "returns": "vocab:dummyClass"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The dummyclass",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "required": "false",
                    "title": "members",
                    "writeonly": "false"
                }
            ],
            "title": "dummyClassCollection"
        },
        {
            "@id": "vocab:extraClassCollection",
            "@type": "hydra:Class",
            "description": "A collection of extraclass",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:extraclass_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all extraClass entities",
                    "expects": "null",
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:extraClassCollection"
                },
                {
                    "@id": "_:extraclass_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new extraClass entity",
                    "expects": "vocab:extraClass",
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "If the extraClass entity was createdsuccessfully.",
                            "statusCode": 201,
                            "title": ""
                        }
                    ],
                    "returns": "vocab:extraClass"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The extraclass",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "required": "false",
                    "title": "members",
                    "writeonly": "false"
                }
            ],
            "title": "extraClassCollection"
        },
        {
            "@id": "vocab:EntryPoint",
            "@type": "hydra:Class",
            "description": "The main entry point or homepage of the API.",
            "supportedOperation": [
                {
                    "@id": "_:entry_point",
                    "@type": "vocab:EntryPoint",
                    "description": "The APIs main entry point.",
                    "expects": "null",
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "null"
                }
            ],
            "supportedProperty": [
                {
                    "hydra:description": "The singleClass Class",
                    "hydra:title": "singleclass",
                    "property": {
                        "@id": "vocab:EntryPoint/singleClass",
                        "@type": "hydra:Link",
                        "description": "A non collection class",
                        "domain": "vocab:EntryPoint",
                        "label": "singleClass",
                        "range": "vocab:singleClass",
                        "supportedOperation": [
                            {
                                "@id": "updateclass",
                                "@type": "http://schema.org/UpdateAction",
                                "description": "null",
                                "expects": "vocab:singleClass",
                                "label": "UpdateClass",
                                "method": "POST",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "",
                                        "statusCode": 200,
                                        "title": "singleClass changed."
                                    }
                                ],
                                "returns": "null"
                            },
                            {
                                "@id": "deleteclass",
                                "@type": "http://schema.org/DeleteAction",
                                "description": "null",
                                "expects": "null",
                                "label": "DeleteClass",
                                "method": "DELETE",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "",
                                        "statusCode": 200,
                                        "title": "singleClass deleted."
                                    }
                                ],
                                "returns": "null"
                            },
                            {
                                "@id": "addclass",
                                "@type": "http://schema.org/AddAction",
                                "description": "null",
                                "expects": "vocab:singleClass",
                                "label": "AddClass",
                                "method": "PUT",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "",
                                        "statusCode": 201,
                                        "title": "singleClass successfully added."
                                    }
                                ],
                                "returns": "null"
                            },
                            {
                                "@id": "getclass",
                                "@type": "http://schema.org/FindAction",
                                "description": "null",
                                "expects": "null",
                                "label": "GetClass",
                                "method": "GET",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "",
                                        "statusCode": 200,
                                        "title": "singleClass returned."
                                    }
                                ],
                                "returns": "vocab:singleClass"
                            }
                        ]
                    },
                    "readonly": "true",
                    "required": "null",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The anotherSingleClass Class",
                    "hydra:title": "anothersingleclass",
                    "property": {
                        "@id": "vocab:EntryPoint/anotherSingleClass",
                        "@type": "hydra:Link",
                        "description": "An another non collection class",
                        "domain": "vocab:EntryPoint",
                        "label": "anotherSingleClass",
                        "range": "vocab:anotherSingleClass",
                        "supportedOperation": [
                            {
                                "@id": "getclass",
                                "@type": "http://schema.org/FindAction",
                                "description": "null",
                                "expects": "null",
                                "label": "GetClass",
                                "method": "GET",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "",
                                        "statusCode": 200,
                                        "title": "anotherSingleClass returned."
                                    }
                                ],
                                "returns": "vocab:anotherSingleClass"
                            }
                        ]
                    },
                    "readonly": "true",
                    "required": "null",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The dummyClassCollection collection",
                    "hydra:title": "dummyclasscollection",
                    "property": {
                        "@id": "vocab:EntryPoint/DcTest",
                        "@type": "hydra:Link",
                        "description": "The dummyClassCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "dummyClassCollection",
                        "range": "vocab:dummyClassCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:dummyclass_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all dummyClass entities",
                                "expects": "null",
                                "method": "GET",
                                "possibleStatus": [],
                                "returns": "vocab:dummyClassCollection"
                            },
                            {
                                "@id": "_:dummyclass_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new dummyClass entity",
                                "expects": "vocab:dummyClass",
                                "method": "PUT",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "If the dummyClass entity was createdsuccessfully.",
                                        "statusCode": 201,
                                        "title": ""
                                    }
                                ],
                                "returns": "vocab:dummyClass"
                            }
                        ]
                    },
                    "readonly": "true",
                    "required": "null",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The extraClassCollection collection",
                    "hydra:title": "extraclasscollection",
                    "property": {
                        "@id": "vocab:EntryPoint/EcTest",
                        "@type": "hydra:Link",
                        "description": "The extraClassCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "extraClassCollection",
                        "range": "vocab:extraClassCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:extraclass_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all extraClass entities",
                                "expects": "null",
                                "method": "GET",
                                "possibleStatus": [],
                                "returns": "vocab:extraClassCollection"
                            },
                            {
                                "@id": "_:extraclass_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new extraClass entity",
                                "expects": "vocab:extraClass",
                                "method": "PUT",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "If the extraClass entity was createdsuccessfully.",
                                        "statusCode": 201,
                                        "title": ""
                                    }
                                ],
                                "returns": "vocab:extraClass"
                            }
                        ]
                    },
                    "readonly": "true",
                    "required": "null",
                    "writeonly": "false"
                }
            ],
            "title": "EntryPoint"
        }
    ],
    "title": "Title for the API Documentation"
}
