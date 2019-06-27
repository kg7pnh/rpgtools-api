book_model = {
    "definitions": {},
    "$id": "http://127.0.0.1:8000/api/v1/schemas/book-model",
    "type": "object",
    "title": "Book",
    "description": "Data required to populate a book class.",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "required": [
        "title",
        "publisher",
        "pages"
    ],
    "properties": {
        "pages": {
            "type": "integer",
            "title": "The Book pages schema",
            "description": "The number of pages in the book.",
            "examples": [
                "23",
                "456"
            ]
        },
        "title": {
            "type": "string",
            "title": "The Book title schema",
            "description": "The title of the book.",
            "examples": [
                "Twilight: 2000, Version 2.2",
                "Dark Conspiracy, 1st Edition"
            ]
        },
        "publisher": {
            "type": "string",
            "title": "The Book publisher schema",
            "minimum": 1,
            "description": "The publisher of the book.",
            "examples": [
                "Palladium Books",
                "Game Designers' Workshop"
            ]
        },
        "short title": {
            "type": "string",
            "title": "The Book short title schema",
            "description": "The short version of the title for the book.",
            "examples": [
                "Twilight: 2000",
                "Dark Conspiracy"
            ]
        },
        "description": {
            "type": "string",
            "title": "The Book description schema",
            "description": "The description of the book.",
            "examples": [
                "Nuclear War has decimated the US, Europe and Asia. You are trying to survive in this new world, where modern technology is dying, roving bands of marauders want your provisions, and radiation is everywhere. Will you survive to find a way home?",
                "Shapes that rip and tear. Shadows that live in corners. Windows in space and time that lead to realms of madness and decay. A dark lurking horror that feeds off the echoing anguish of a billion tortured souls. This is the center of a twisted, sinister conspiracy which threatens the very existence of all humankind. Set in the near future, the world of Dark Conspiracy is dramatically altered from today and is fraught with peril and challenges. The Metroplexes, where most of the world's population lives, are a blend of lawless gang turf and corporate fortresses ruled by men and women powerful enough to be above the law. The countryside is sparsely inhabited, its natives suspicious and violent. And increasing areas of countryside are turning into Demonground, from which few humans return."
            ]
        },
        "format": {
            "type": "string",
            "title": "The Book format schema",
            "description": "The format the book was published in.",            
            "enum": [
                "soft cover",
                "hard cover",
                "magazine",
                "pdf",
                "epub",
                "mobi"
            ]
        },
        "catalog number": {
            "type": "string",
            "title": "The Book catalog number schema",
            "description": "The catalog number associated with the book from the publisher.",
            "examples": [
                "2000",
                "2100",
                "800-HC"
            ]
        },
        "isbn 10": {
            "type": "string",
            "title": "The Book ISBN-10 schema",
            "description": "The ISBN-10 number assigned to the book.",
            "examples": [
                "1558780769",
                "ISBN 1558780769",
                "ISBN10 1558780769",
                "ISBN-10 1558780769"
            ],
            "pattern": "^(?:ISBN(?:10)?(?:\\-10)?\\x20)?[0-9]{9}(\\d|X)$"
        },
        "isbn 13": {
            "type": "string",
            "title": "The Book ISBN-13 schema",
            "description": "The ISBN-13 number assigned to the book.",
            "examples": [
                "9781558780767",
                "ISBN 9781558780767",
                "ISBN13 9781558780767",
                "ISBN-13 9781558780767"
            ],
            "pattern": "^(?:ISBN(?:13)?(?:\\-13)?\\x20)?:?97(?:8|9)[0-9]{10}$"
        }
    }
}