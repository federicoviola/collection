"""

Collection
Copyright (c) 2013 Zachary King

---------------------------------------------------------------------------
Based on https://github.com/Mendeley/mendeley-oapi-example

Mendeley Open API Example Client

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

For details of the Mendeley Open API see http://dev.mendeley.com/
---------------------------------------------------------------------------
"""


import sys, requests, json, oauth2

import mendeley_client

mendeley = mendeley_client.create_client()

# get folder name
if len(sys.argv) < 2:
    raise Exception('needs folder name argument')
folder_name = sys.argv[1]

# get folder documents
folders = mendeley.folders()

folder_id = None
for folder in folders:
    if folder['name'] == folder_name:
        folder_id = folder['id']
if folder_id == None:
    raise Exception('Folder not found')

# get folder documents
docs = mendeley.folder_documents(folder_id)

for doc_id in docs['document_ids']:
    details = mendeley.document_details(doc_id)
    print(details)
