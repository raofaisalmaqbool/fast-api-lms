"""Section and ContentBlock API routes."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/{section_id}")
async def read_section(section_id: int):
    """Get a section by ID (not yet implemented)."""
    return {"message": "Section endpoint not yet implemented"}


@router.get("/{section_id}/content-blocks")
async def read_section_content_blocks(section_id: int):
    """Get content blocks for a section (not yet implemented)."""
    return {"message": "Content blocks endpoint not yet implemented"}


@router.get("/content-blocks/{block_id}")
async def read_content_block(block_id: int):
    """Get a content block by ID (not yet implemented)."""
    return {"message": "Content block endpoint not yet implemented"}
