def validate_file_extension(file_path, valid_extensions):
    """Check if file has one of the valid extensions"""
    return any(file_path.lower().endswith(ext) for ext in valid_extensions)