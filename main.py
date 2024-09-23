# importation des modules 
from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas 

from .db import SessionLocal, engine
# creation d'un moteur sqlalchemy
models.Base.metadata.create_all(bind=engine)
# instanciation d'un objet fastapi
app = FastAPI()

# Définir une dépendance pour la session de la base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# endpoint pour ajouter des taches
@app.post("/tasks/", response_model=schemas.Task)
async def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)
# endpoint pour recuperer des taches
@app.get("/tasks/", response_model=List[schemas.Task])
async def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db, skip=skip, limit=limit)
    return tasks
# endpoint pour recuperer des taches par l'ID
@app.get("/tasks/{task_id}", response_model=schemas.Task)
async def read_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
# endpoint pour modifier des taches par l'ID
@app.put("/tasks/{task_id}", response_model=schemas.Task)
async def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task = crud.update_task(db, task_id=task_id, task=task)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
# endpoint pour supprimer des taches par l'ID

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}