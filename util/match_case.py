status = 404
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")  # выполнится этот блок
    case 500:
        print("Server Error")
    case _:
        print("Other status")