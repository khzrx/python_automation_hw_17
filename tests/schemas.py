single_user = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "email": {
                    "type": "string"
                },
                "first_name": {
                    "type": "string"
                },
                "last_name": {
                    "type": "string"
                },
                "avatar": {
                    "type": "string"
                }
            },
            "required": [
                "id",
                "email",
                "first_name",
                "last_name",
                "avatar"
            ]
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string"
                },
                "text": {
                    "type": "string"
                }
            },
            "required": [
                "url",
                "text"
            ]
        }
    },
    "required": [
        "data",
        "support"
    ]
}

unauthorized_error = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "error": {
      "type": "string"
    }
  },
  "required": [
    "error"
  ]
}

users_post = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "job": {
            "type": "string"
        },
        "id": {
            "type": "string"
        },
        "createdAt": {
            "type": "string"
        }
    },
    "required": [
        "name",
        "job",
        "id",
        "createdAt"
    ]
}

users_put = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "job": {
      "type": "string"
    },
    "updatedAt": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "job",
    "updatedAt"
  ]
}