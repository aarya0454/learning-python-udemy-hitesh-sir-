def serve_chai(flavor):
    try:
        print(f"Preaparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("we don't know that flavor")
    except ValueError as e:
        print("error: ", e)
    else:
        print(f"{flavor} chai is served")
    finally:
        print("Next coustomer please")
serve_chai("masala")