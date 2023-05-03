from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

transaction_repository.delete_all()
merchant_repository.delete_all()
tag_repository.delete_all()

tag1 = Tag("Food")
tag_repository.save(tag1)

merchant1 = Merchant("Tesco")
merchant_repository.save(merchant1)

transaction1 = Transaction(100, merchant1, tag1)
transaction_repository.save(transaction1)