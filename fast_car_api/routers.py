from fastapi import APIRouter

router = APIRouter(
    prefix = '/api/v1/cars',
    tags = ['cars']
)

@router.get('/')
def list_car():
    return{
        'cars': [
            {'id': 1, 'modelo': 'marea 20v'},
            {'id': 2, 'modelo': 'opala'},
            {'id': 3, 'modelo': 'corsa'},
        ]
    }