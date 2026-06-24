from sqlalchemy.engine import Connection
from fastapi import HTTPException, status
from ..repos import reactions_repo
from ..schemas.reactions_schema import ReactionCreate, ReactionDelete

def add_or_update_reaction(
    conn: Connection,
    reaction_data: ReactionCreate,
    current_user
):
    # Check if target exists
    target_exists = reactions_repo.check_target_exists(
        conn=conn,
        target_type=reaction_data.target_type,
        target_id=reaction_data.target_id
    )
    
    if not target_exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{reaction_data.target_type.capitalize()} not found"
        )
    
    # Add or update the reaction
    rows_affected = reactions_repo.add_or_update_reaction(
        conn=conn,
        user_id=current_user['id'],
        reaction_data=reaction_data
    )
    
    if rows_affected == 0:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to save reaction"
        )
    
    return {"message": "Reaction saved"}

def remove_reaction(
    conn: Connection,
    reaction_data: ReactionDelete,
    current_user
):
    rows_deleted = reactions_repo.remove_reaction(
        conn=conn,
        user_id=current_user['id'],
        reaction_data=reaction_data
    )
    
    if rows_deleted == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reaction not found"
        )
    
    return {"message": "Reaction removed"}

def get_reaction_stats(
    conn: Connection,
    target_type: str,
    target_id: int
):
    # Validate target type
    if target_type not in ['prompt', 'comment']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid target_type. Must be 'prompt' or 'comment'"
        )
    
    # Check if target exists
    target_exists = reactions_repo.check_target_exists(
        conn=conn,
        target_type=target_type,
        target_id=target_id
    )
    
    if not target_exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{target_type.capitalize()} not found"
        )
    
    stats = reactions_repo.get_reaction_stats(
        conn=conn,
        target_type=target_type,
        target_id=target_id
    )
    
    return stats
