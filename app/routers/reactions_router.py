from fastapi import APIRouter, Depends, Query, status
from typing import Annotated
from ..auth import dbConn, get_current_user
from ..services import reactions_service
from ..schemas.reactions_schema import ReactionCreate, ReactionDelete, ReactionStats

router = APIRouter(tags=['reactions'])

@router.post("/reactions", status_code=status.HTTP_201_CREATED)
def add_or_update_reaction(
    conn: dbConn,
    reaction_data: ReactionCreate,
    current_user=Depends(get_current_user)
):
    """
    Add or update a reaction (like/dislike) on a prompt or comment.
    If user already reacted, this will update their reaction.
    """
    return reactions_service.add_or_update_reaction(
        conn=conn,
        reaction_data=reaction_data,
        current_user=current_user
    )

@router.delete("/reactions")
def remove_reaction(
    conn: dbConn,
    reaction_data: ReactionDelete,
    current_user=Depends(get_current_user)
):
    """
    Remove user's reaction from a prompt or comment.
    """
    return reactions_service.remove_reaction(
        conn=conn,
        reaction_data=reaction_data,
        current_user=current_user
    )

@router.get("/reactions", response_model=ReactionStats)
def get_reaction_stats(
    conn: dbConn,
    target_type: Annotated[str, Query(pattern="^(prompt|comment)$")],
    target_id: Annotated[int, Query(gt=0)]
):
    """
    Get reaction statistics (like/dislike counts) for a prompt or comment.
    No authentication required - public endpoint.
    """
    return reactions_service.get_reaction_stats(
        conn=conn,
        target_type=target_type,
        target_id=target_id
    )
