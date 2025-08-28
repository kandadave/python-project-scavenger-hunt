def format_object(obj):
    if not obj:
        return "Not found"
    if obj.__class__.__name__ == "Quest":
        return (f"| ID: {obj.id} | Name: {obj.name} | Location: {obj._location} | "
                f"Type: {obj._type} | Clue: {obj.clue} | Created: {obj.created_at} |")
    return "\n".join(f"{key}: {value}" for key, value in vars(obj).items() if not key.startswith("_sa_"))