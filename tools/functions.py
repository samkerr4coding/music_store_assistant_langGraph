functions = [
    {
        "name": "get_track_by_id",
        "description": "Retrieve a track from the database based on its ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "track_id": {
                    "type": "integer",
                    "description": "The ID of the track to retrieve."
                }
            },
            "required": ["track_id"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object"
            },
            "description": "A list of track records matching the given ID."
        }
    },
    {
        "name": "get_tracks_by_album_title",
        "description": "Retrieve all tracks from the database that belong to albums with titles matching the given string.",
        "parameters": {
            "type": "object",
            "properties": {
                "album_title": {
                    "type": "string",
                    "description": "The title of the album to search for."
                }
            },
            "required": ["album_title"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object"
            },
            "description": "A list of tracks belonging to albums with titles that match the given string."
        }
    },
    {
        "name": "get_tracks_by_artist_name",
        "description": "Retrieve all tracks from the database by artists whose names match the given string.",
        "parameters": {
            "type": "object",
            "properties": {
                "artist_name": {
                    "type": "string",
                    "description": "The name of the artist to search for."
                }
            },
            "required": ["artist_name"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object"
            },
            "description": "A list of tracks by artists whose names match the given string."
        }
    },
    {
        "name": "insert_track",
        "description": "Insert a new track into the database.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "The name of the track."},
                "album_id": {"type": "integer", "description": "The ID of the album to which the track belongs."},
                "media_type_id": {"type": "integer", "description": "The media type ID of the track."},
                "genre_id": {"type": "integer", "description": "The genre ID of the track."},
                "composer": {"type": "string", "description": "The composer of the track."},
                "milliseconds": {"type": "integer", "description": "The duration of the track in milliseconds."},
                "bytes": {"type": "integer", "description": "The size of the track in bytes."},
                "unit_price": {"type": "number", "description": "The price of the track."}
            },
            "required": ["name", "album_id", "media_type_id", "genre_id", "composer", "milliseconds", "bytes", "unit_price"]
        }
    },
    {
        "name": "update_track",
        "description": "Update an existing track in the database based on its ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "track_id": {"type": "integer", "description": "The ID of the track to update."},
                "name": {"type": "string", "description": "The new name of the track."},
                "album_id": {"type": "integer", "description": "The new album ID for the track."},
                "media_type_id": {"type": "integer", "description": "The new media type ID for the track."},
                "genre_id": {"type": "integer", "description": "The new genre ID for the track."},
                "composer": {"type": "string", "description": "The new composer of the track."},
                "milliseconds": {"type": "integer", "description": "The new duration of the track in milliseconds."},
                "bytes": {"type": "integer", "description": "The new size of the track in bytes."},
                "unit_price": {"type": "number", "description": "The new price of the track."}
            },
            "required": ["track_id", "name", "album_id", "media_type_id", "genre_id", "composer", "milliseconds", "bytes", "unit_price"]
        }
    },
    {
        "name": "delete_track",
        "description": "Delete a track from the database based on its ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "track_id": {
                    "type": "integer",
                    "description": "The ID of the track to delete."
                }
            },
            "required": ["track_id"]
        }
    },
    {
        "name": "get_album_by_id",
        "description": "Retrieve an album from the database based on its ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "album_id": {
                    "type": "integer",
                    "description": "The ID of the album to retrieve."
                }
            },
            "required": ["album_id"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object"
            },
            "description": "A list of album records matching the given ID."
        }
    },
    {
        "name": "get_albums_by_artist_name",
        "description": "Retrieve all albums from the database by artists whose names match the given string.",
        "parameters": {
            "type": "object",
            "properties": {
                "artist_name": {
                    "type": "string",
                    "description": "The name of the artist to search for."
                }
            },
            "required": ["artist_name"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object"
            },
            "description": "A list of albums by artists whose names match the given string."
        }
    },
    {
        "name": "get_albums_by_title",
        "description": "Retrieve all albums from the database with titles matching the given string.",
        "parameters": {
            "type": "object",
            "properties": {
                "album_title": {
                    "type": "string",
                    "description": "The title of the album to search for."
                }
            },
            "required": ["album_title"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object"
            },
            "description": "A list of albums with titles that match the given string."
        }
    },
    {
        "name": "insert_album",
        "description": "Insert a new album into the database.",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {"type": "string", "description": "The title of the album."},
                "artist_id": {"type": "integer", "description": "The ID of the artist who created the album."}
            },
            "required": ["title", "artist_id"]
        }
    },
    {
        "name": "update_album",
        "description": "Update an existing album in the database based on its ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "album_id": {"type": "integer", "description": "The ID of the album to update."},
                "title": {"type": "string", "description": "The new title of the album."},
                "artist_id": {"type": "integer", "description": "The new artist ID for the album."}
            },
            "required": ["album_id", "title", "artist_id"]
        }
    },
    {
        "name": "delete_album",
        "description": "Delete an album from the database based on its ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "album_id": {
                    "type": "integer",
                    "description": "The ID of the album to delete."
                }
            },
            "required": ["album_id"]
        }
    },
    {
        "name": "get_artist_by_id",
        "description": "Retrieve an artist from the database based on their ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "artist_id": {
                    "type": "integer",
                    "description": "The ID of the artist to retrieve."
                }
            },
            "required": ["artist_id"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object"
            },
            "description": "A list of artist records matching the given ID."
        }
    },
    {
        "name": "get_artist_by_name",
        "description": "Retrieve an artist from the database whose name matches the given string.",
        "parameters": {
            "type": "object",
            "properties": {
                "artist_name": {
                    "type": "string",
                    "description": "The name of the artist to search for."
                }
            },
            "required": ["artist_name"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object"
            },
            "description": "A list of artist records whose names match the given string."
        }
    },
{
        "name": "insert_artist",
        "description": "Insert a new artist into the database.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The name of the artist."
                }
            },
            "required": ["name"]
        }
    },
    {
        "name": "update_artist",
        "description": "Update an existing artist in the database based on their ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "artist_id": {
                    "type": "integer",
                    "description": "The ID of the artist to update."
                },
                "name": {
                    "type": "string",
                    "description": "The new name of the artist."
                }
            },
            "required": ["artist_id", "name"]
        }
    },
    {
        "name": "delete_artist",
        "description": "Delete an artist from the database based on their ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "artist_id": {
                    "type": "integer",
                    "description": "The ID of the artist to delete."
                }
            },
            "required": ["artist_id"]
        }
    },
    {
        "name": "get_customer_by_id",
        "description": "Retrieve a customer from the database based on their ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "integer",
                    "description": "The ID of the customer to retrieve."
                }
            },
            "required": ["customer_id"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object"
            },
            "description": "A list of customer records matching the given ID."
        }
    },
    {
        "name": "get_customers_by_name",
        "description": "Retrieve all customers from the database whose names match the given string.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "The name of the customer to search for."
                }
            },
            "required": ["customer_name"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object"
            },
            "description": "A list of customers whose names match the given string."
        }
    },
    {
        "name": "get_customers_by_email",
        "description": "Retrieve all customers from the database whose email addresses match the given string.",
        "parameters": {
            "type": "object",
            "properties": {
                "email": {
                    "type": "string",
                    "description": "The email address to search for."
                }
            },
            "required": ["email"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object"
            },
            "description": "A list of customers whose email addresses match the given string."
        }
    },
    {
        "name": "insert_customer",
        "description": "Insert a new customer into the database.",
        "parameters": {
            "type": "object",
            "properties": {
                "first_name": {"type": "string", "description": "The first name of the customer."},
                "last_name": {"type": "string", "description": "The last name of the customer."},
                "company": {"type": "string", "description": "The company of the customer."},
                "address": {"type": "string", "description": "The address of the customer."},
                "city": {"type": "string", "description": "The city of the customer."},
                "state": {"type": "string", "description": "The state of the customer."},
                "country": {"type": "string", "description": "The country of the customer."},
                "postal_code": {"type": "string", "description": "The postal code of the customer."},
                "phone": {"type": "string", "description": "The phone number of the customer."},
                "fax": {"type": "string", "description": "The fax number of the customer."},
                "email": {"type": "string", "description": "The email address of the customer."},
                "support_rep_id": {"type": "integer", "description": "The ID of the support representative assigned to the customer."}
            },
            "required": ["first_name", "last_name", "company", "address", "city", "state", "country", "postal_code", "phone", "fax", "email", "support_rep_id"]
        }
    },
    {
        "name": "update_customer",
        "description": "Update an existing customer in the database based on their ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {"type": "integer", "description": "The ID of the customer to update."},
                "first_name": {"type": "string", "description": "The new first name of the customer."},
                "last_name": {"type": "string", "description": "The new last name of the customer."},
                "company": {"type": "string", "description": "The new company of the customer."},
                "address": {"type": "string", "description": "The new address of the customer."},
                "city": {"type": "string", "description": "The new city of the customer."},
                "state": {"type": "string", "description": "The new state of the customer."},
                "country": {"type": "string", "description": "The new country of the customer."},
                "postal_code": {"type": "string", "description": "The new postal code of the customer."},
                "phone": {"type": "string", "description": "The new phone number of the customer."},
                "fax": {"type": "string", "description": "The new fax number of the customer."},
                "email": {"type": "string", "description": "The new email address of the customer."},
                "support_rep_id": {"type": "integer", "description": "The new ID of the support representative assigned to the customer."}
            },
            "required": ["customer_id", "first_name", "last_name", "company", "address", "city", "state", "country", "postal_code", "phone", "fax", "email", "support_rep_id"]
        }
    },
    {
        "name": "delete_customer",
        "description": "Delete a customer from the database based on their ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "integer",
                    "description": "The ID of the customer to delete."
                }
            },
            "required": ["customer_id"]
        }
    },
    {
        "name": "get_invoice_by_id",
        "description": "Retrieve an invoice from the database based on its ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "invoice_id": {
                    "type": "integer",
                    "description": "The ID of the invoice to retrieve."
                }
            },
            "required": ["invoice_id"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object"
            },
            "description": "A list of invoice records matching the given ID."
        }
    },
    {
        "name": "get_invoices_by_customer_name",
        "description": "Retrieve all invoices from the database for customers whose names match the given string.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "The name of the customer to search for."
                }
            },
            "required": ["customer_name"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object"
            },
            "description": "A list of invoices for customers whose names match the given string."
        }
    },
    {
        "name": "insert_invoice",
        "description": "Insert a new invoice into the database.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {"type": "integer", "description": "The ID of the customer associated with the invoice."},
                "invoice_date": {"type": "string", "description": "The date of the invoice."},
                "billing_address": {"type": "string", "description": "The billing address for the invoice."},
                "billing_city": {"type": "string", "description": "The billing city for the invoice."},
                "billing_state": {"type": "string", "description": "The billing state for the invoice."},
                "billing_country": {"type": "string", "description": "The billing country for the invoice."},
                "billing_postal_code": {"type": "string", "description": "The billing postal code for the invoice."},
                "total": {"type": "number", "description": "The total amount of the invoice."}
            },
            "required": ["customer_id", "invoice_date", "billing_address", "billing_city", "billing_state", "billing_country", "billing_postal_code", "total"]
        }
    },
    {
        "name": "update_invoice",
        "description": "Update an existing invoice in the database based on its ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "invoice_id": {"type": "integer", "description": "The ID of the invoice to update."},
                "customer_id": {"type": "integer", "description": "The ID of the customer associated with the invoice."},
                "invoice_date": {"type": "string", "description": "The new date of the invoice."},
                "billing_address": {"type": "string", "description": "The new billing address for the invoice."},
                "billing_city": {"type": "string", "description": "The new billing city for the invoice."},
                "billing_state": {"type": "string", "description": "The new billing state for the invoice."},
                "billing_country": {"type": "string", "description": "The new billing country for the invoice."},
                "billing_postal_code": {"type": "string", "description": "The new billing postal code for the invoice."},
                "total": {"type": "number", "description": "The new total amount of the invoice."}
            },
            "required": ["invoice_id", "customer_id", "invoice_date", "billing_address", "billing_city", "billing_state", "billing_country", "billing_postal_code", "total"]
        }
    },
    {
        "name": "delete_invoice",
        "description": "Delete an invoice from the database based on its ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "invoice_id": {
                    "type": "integer",
                    "description": "The ID of the invoice to delete."
                }
            },
            "required": ["invoice_id"]
        }
    },
    {
        "name": "get_employee_by_id",
        "description": "Retrieve an employee from the database based on their ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_id": {
                    "type": "integer",
                    "description": "The ID of the employee to retrieve."
                }
            },
            "required": ["employee_id"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object"
            },
            "description": "A list of employee records matching the given ID."
        }
    },
    {
        "name": "get_employees_by_name",
        "description": "Retrieve all employees from the database whose names match the given string.",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_name": {
                    "type": "string",
                    "description": "The name of the employee to search for."
                }
            },
            "required": ["employee_name"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object"
            },
            "description": "A list of employees whose names match the given string."
        }
    },
    {
        "name": "insert_employee",
        "description": "Insert a new employee into the database.",
        "parameters": {
            "type": "object",
            "properties": {
                "last_name": {"type": "string", "description": "The last name of the employee."},
                "first_name": {"type": "string", "description": "The first name of the employee."},
                "title": {"type": "string", "description": "The job title of the employee."},
                "reports_to": {"type": "integer", "description": "The ID of the employee's manager."},
                "birth_date": {"type": "string", "description": "The birth date of the employee."},
                "hire_date": {"type": "string", "description": "The hire date of the employee."},
                "address": {"type": "string", "description": "The address of the employee."},
                "city": {"type": "string", "description": "The city of the employee."},
                "state": {"type": "string", "description": "The state of the employee."},
                "country": {"type": "string", "description": "The country of the employee."},
                "postal_code": {"type": "string", "description": "The postal code of the employee."},
                "phone": {"type": "string", "description": "The phone number of the employee."},
                "fax": {"type": "string", "description": "The fax number of the employee."},
                "email": {"type": "string", "description": "The email address of the employee."}
            },
            "required": ["last_name", "first_name", "title", "reports_to", "birth_date", "hire_date", "address", "city", "state", "country", "postal_code", "phone", "fax", "email"]
        }
    },
    {
        "name": "update_employee",
        "description": "Update an existing employee in the database based on their ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_id": {"type": "integer", "description": "The ID of the employee to update."},
                "last_name": {"type": "string", "description": "The new last name of the employee."},
                "first_name": {"type": "string", "description": "The new first name of the employee."},
                "title": {"type": "string", "description": "The new job title of the employee."},
                "reports_to": {"type": "integer", "description": "The new ID of the employee's manager."},
                "birth_date": {"type": "string", "description": "The new birth date of the employee."},
                "hire_date": {"type": "string", "description": "The new hire date of the employee."},
                "address": {"type": "string", "description": "The new address of the employee."},
                "city": {"type": "string", "description": "The new city of the employee."},
                "state": {"type": "string", "description": "The new state of the employee."},
                "country": {"type": "string", "description": "The new country of the employee."},
                "postal_code": {"type": "string", "description": "The new postal code of the employee."},
                "phone": {"type": "string", "description": "The new phone number of the employee."},
                "fax": {"type": "string", "description": "The new fax number of the employee."},
                "email": {"type": "string", "description": "The new email address of the employee."}
            },
            "required": ["employee_id", "last_name", "first_name", "title", "reports_to", "birth_date", "hire_date", "address", "city", "state", "country", "postal_code", "phone", "fax", "email"]
        }
    },
    {
        "name": "delete_employee",
        "description": "Delete an employee from the database based on their ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_id": {
                    "type": "integer",
                    "description": "The ID of the employee to delete."
                }
            },
            "required": ["employee_id"]
        }
    },
    {
        "name": "get_playlist_by_id",
        "description": "Retrieve a playlist from the database based on its ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "playlist_id": {
                    "type": "integer",
                    "description": "The ID of the playlist to retrieve."
                }
            },
            "required": ["playlist_id"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object",
                "description": "A list of playlist records matching the given ID."
            }
        }
    },
    # {
    #     "name": "get_playlists_by_name",
    #     "description": "Retrieve all playlists from the database whose names match the given string.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "playlist_name": {
    #                 "type": "string",
    #                 "description": "The name of the playlist to search for."
    #             }
    #         },
    #         "required": ["playlist_name"]
    #     },
    #     "returns": {
    #         "type": "array",
    #         "items": {
    #             "type": "object",
    #             "description": "A list of playlists whose names match the given string."
    #         }
    #     }
    # },
    {
        "name": "insert_playlist",
        "description": "Insert a new playlist into the database.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The name of the new playlist."
                }
            },
            "required": ["name"]
        },
        "returns": {
            "type": "null"
        }
    },
    {
        "name": "update_playlist",
        "description": "Update an existing playlist in the database based on its ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "playlist_id": {
                    "type": "integer",
                    "description": "The ID of the playlist to update."
                },
                "name": {
                    "type": "string",
                    "description": "The new name of the playlist."
                }
            },
            "required": ["playlist_id", "name"]
        },
        "returns": {
            "type": "null"
        }
    },
    {
        "name": "delete_playlist",
        "description": "Delete a playlist from the database based on its ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "playlist_id": {
                    "type": "integer",
                    "description": "The ID of the playlist to delete."
                }
            },
            "required": ["playlist_id"]
        },
        "returns": {
            "type": "null"
        }
    },
{
        "name": "get_playlists_by_composer_name",
        "description": "Retrieve playlists containing tracks by a given composer.",
        "parameters": {
            "type": "object",
            "properties": {
                "artist_name": {
                    "type": "string",
                    "description": "The name of the artist to search for."
                }
            },
            "required": ["artist_name"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object",
                "description": "A list of playlists containing tracks by the given artist."
            }
        }
    },
    {
        "name": "get_playlists_by_song_name",
        "description": "Retrieve playlists containing a specific song.",
        "parameters": {
            "type": "object",
            "properties": {
                "song_name": {
                    "type": "string",
                    "description": "The name of the song to search for."
                }
            },
            "required": ["song_name"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object",
                "description": "A list of playlists containing the specified song."
            }
        }
    },
    {
        "name": "get_playlists_by_genre",
        "description": "Retrieve playlists containing tracks of a specific genre.",
        "parameters": {
            "type": "object",
            "properties": {
                "genre_name": {
                    "type": "string",
                    "description": "The name of the genre to search for."
                }
            },
            "required": ["genre_name"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object",
                "description": "A list of playlists containing tracks of the specified genre."
            }
        }
    },
    {
        "name": "get_playlists_by_album_name",
        "description": "Retrieve playlists containing tracks from a specific album.",
        "parameters": {
            "type": "object",
            "properties": {
                "album_name": {
                    "type": "string",
                    "description": "The name of the album to search for."
                }
            },
            "required": ["album_name"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object",
                "description": "A list of playlists containing tracks from the specified album."
            }
        }
    },
    {
        "name": "get_playlists_by_playlist_name",
        "description": "Retrieve playlists matching a specific name.",
        "parameters": {
            "type": "object",
            "properties": {
                "playlist_name": {
                    "type": "string",
                    "description": "The name of the playlist to search for."
                }
            },
            "required": ["playlist_name"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object",
                "description": "A list of playlists matching the specified name."
            }
        }
    },
    {
        "name": "get_invoice_line_by_id",
        "description": "Retrieve an invoice line from the database based on its ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "invoice_line_id": {
                    "type": "integer",
                    "description": "The ID of the invoice line to retrieve."
                }
            },
            "required": ["invoice_line_id"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object",
                "description": "A list of invoice line records matching the given ID."
            }
        }
    },
    {
        "name": "get_invoice_lines_by_invoice_id",
        "description": "Retrieve all invoice lines from the database for a given invoice ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "invoice_id": {
                    "type": "integer",
                    "description": "The ID of the invoice to retrieve lines for."
                }
            },
            "required": ["invoice_id"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object",
                "description": "A list of invoice lines associated with the given invoice ID."
            }
        }
    },
    {
        "name": "insert_invoice_line",
        "description": "Insert a new invoice line into the database.",
        "parameters": {
            "type": "object",
            "properties": {
                "invoice_id": {
                    "type": "integer",
                    "description": "The ID of the invoice to associate the line with."
                },
                "track_id": {
                    "type": "integer",
                    "description": "The ID of the track included in the invoice line."
                },
                "unit_price": {
                    "type": "number",
                    "format": "float",
                    "description": "The unit price of the track."
                },
                "quantity": {
                    "type": "integer",
                    "description": "The quantity of the track purchased."
                }
            },
            "required": ["invoice_id", "track_id", "unit_price", "quantity"]
        },
        "returns": {
            "type": "null"
        }
    },
    {
        "name": "update_invoice_line",
        "description": "Update an existing invoice line in the database based on its ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "invoice_line_id": {
                    "type": "integer",
                    "description": "The ID of the invoice line to update."
                },
                "invoice_id": {
                    "type": "integer",
                    "description": "The ID of the invoice to associate the updated line with."
                },
                "track_id": {
                    "type": "integer",
                    "description": "The ID of the track included in the updated invoice line."
                },
                "unit_price": {
                    "type": "number",
                    "format": "float",
                    "description": "The new unit price of the track."
                },
                "quantity": {
                    "type": "integer",
                    "description": "The new quantity of the track purchased."
                }
            },
            "required": ["invoice_line_id", "invoice_id", "track_id", "unit_price", "quantity"]
        },
        "returns": {
            "type": "null"
        }
    },
    {
        "name": "delete_invoice_line",
        "description": "Delete an invoice line from the database based on its ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "invoice_line_id": {
                    "type": "integer",
                    "description": "The ID of the invoice line to delete."
                }
            },
            "required": ["invoice_line_id"]
        },
        "returns": {
            "type": "null"
        }
    },
    {
        "name": "get_genre_by_id",
        "description": "Retrieve a genre from the database based on its ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "genre_id": {
                    "type": "integer",
                    "description": "The ID of the genre to retrieve."
                }
            },
            "required": ["genre_id"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object",
                "description": "A list of genre records matching the given ID."
            }
        }
    },
    {
        "name": "get_genres_by_name",
        "description": "Retrieve all genres from the database whose names match the given string.",
        "parameters": {
            "type": "object",
            "properties": {
                "genre_name": {
                    "type": "string",
                    "description": "The name of the genre to search for."
                }
            },
            "required": ["genre_name"]
        },
        "returns": {
            "type": "array",
            "items": {
                "type": "object",
                "description": "A list of genres whose names match the given string."
            }
        }
    },
    {
        "name": "insert_genre",
        "description": "Insert a new genre into the database.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The name of the new genre."
                }
            },
            "required": ["name"]
        },
        "returns": {
            "type": "null"
        }
    },
    {
        "name": "update_genre",
        "description": "Update an existing genre in the database based on its ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "genre_id": {
                    "type": "integer",
                    "description": "The ID of the genre to update."
                },
                "name": {
                    "type": "string",
                    "description": "The new name of the genre."
                }
            },
            "required": ["genre_id", "name"]
        },
        "returns": {
            "type": "null"
        }
    },
    {
        "name": "delete_genre",
        "description": "Delete a genre from the database based on its ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "genre_id": {
                    "type": "integer",
                    "description": "The ID of the genre to delete."
                }
            },
            "required": ["genre_id"]
        },
        "returns": {
            "type": "null"
        }
    }
]
