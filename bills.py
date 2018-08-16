import boto3


class Bills:
    def __init__(self):
        self.bills = boto3.resource('dynamodb', region_name='us-east-1').Table('bills')

    def insert(self, introductions):
        with self.bills.batch_writer() as batch:
            for introduction in introductions:
                batch.put_item(
                    Item={'bill_id': introduction.identifier,
                          'title': introduction.title,
                          'classification': introduction.classifications,
                          'legistar_url': introduction.legistar_url,
                          }
                )

    def exists(self, hash_key):
        response = self.bills.get_item(
            Key={'bill_id': hash_key}
        )
        if 'Item' in response:
            return True
        return False
