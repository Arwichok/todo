from litestar.dto import DTOConfig


create_config = DTOConfig(
    exclude={"created_at", "updated_at", "id"},
)