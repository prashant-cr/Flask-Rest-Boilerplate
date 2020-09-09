from models import session
from tables.bank import BankTable


def get_bank_info(bank_id):
    """
    This method is used to get bank info using the bank id
    :param bank_id:
    :return: returning the dict of bank information
    """
    if bank_id:
        result = session.query(BankTable).filter(
            BankTable.id == bank_id,
            BankTable.is_deleted == 0
        ).first()
        if result:
            result_set = {"bank_name": result.name, "id": result.id, "address": result.address,
                          "mobile_number": result.mobile_number, "bank_manager": result.bank_manager}
        else:
            raise ValueError("No-Entry-Found")
    else:
        result = session.query(BankTable).filter(
            BankTable.is_deleted == 0
        ).all()

        result_array = []
        for bank in result:
            temp_dict = dict()
            temp_dict["bank_name"] = bank.name
            temp_dict["id"] = bank.id
            temp_dict["address"] = bank.address
            temp_dict["mobile_number"] = bank.mobile_number
            temp_dict["bank_manager"] = bank.bank_manager
            result_array.append(temp_dict)
        result_set = dict(result=result_array, status=True)
    return result_set


def post_bank_info(**kwargs):
    """
    This method is used to insert entry to the database
    :param kwargs:
    :return: return with id and status
    """
    bank_info = BankTable(**kwargs)
    session.add(bank_info)
    session.flush()
    return dict(id=bank_info.id, status=True)


def put_bank_info(**kwargs):
    """
    This method is used to update the bank table row
    :param kwargs:
    :return: return id and status
    """
    bank_id = kwargs.pop('bank_id')
    update_dict = dict()
    if kwargs.get('name'):
        update_dict.update(name=kwargs.get("name"))
    if kwargs.get('address'):
        update_dict.update(address=kwargs.get("address"))
    if kwargs.get('mobile_number'):
        update_dict.update(mobile_number=kwargs.get("mobile_number"))
    if kwargs.get('bank_manager'):
        update_dict.update(bank_manager=kwargs.get("bank_manager"))
    session.query(BankTable).filter(
        BankTable.id == bank_id,
        BankTable.is_deleted == 0
    ).update(update_dict)
    session.flush()
    return dict(status=True)


def delete_bank_info(bank_id):
    """
    This method is used to delete the entry from bank info
    :param bank_id:
    :return:
    """
    session.query(BankTable).filter(
        BankTable.id == bank_id,
        BankTable.is_deleted == 0
    ).update({"is_deleted": 1})
    session.flush()
    return dict(status=True)
