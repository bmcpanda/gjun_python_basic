def _save_database(info_dictionary):
    print("save to DB complete!", info_dictionary)

#會員系統流程
def handle_membership_creation(name, id, phone, *hobbies, **other_information):
    gender = other_information['gender'] if 'gender' in other_information else "unknown"
    age = other_information['age'] if 'age' in other_information else "Unknown"
    member_information = {
        'member_name' : name,
        'member_personal_id' : id,
        'member_cellphone_number' : phone,
        'member_hobby': hobbies,
        'member_gender': gender,
        'member_age': age,

    }

    _save_database(info_dictionary=member_information)

if __name__ == '__main__':
    hobby = ['coding', 'biking', 'video game']
    info = {
            'gender' : 'male',
            'age' : 30,
            'born_city': 'Taichung'
    }
    handle_membership_creation("chung yi", 'B1263545645', '0912345678', *hobby, **info)