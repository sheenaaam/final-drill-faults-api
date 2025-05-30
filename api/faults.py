from flask import Blueprint, request, jsonify
from models import db, Fault
from datetime import datetime

# Define the blueprint
faults_bp = Blueprint('faults', __name__, url_prefix='/api/faults')

# Create a fault (POST)
@faults_bp.route('/', methods=['POST'])
def create_fault():
    data = request.get_json()
    try:
        fault = Fault(
            student_id=data['student_id'],
            description=data['description'],
            date_reported=datetime.strptime(data['date_reported'], '%Y-%m-%d'),
            resolved=data.get('resolved', False)
        )
        db.session.add(fault)
        db.session.commit()
        return jsonify({'message': 'Fault reported successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Read all faults (GET)
@faults_bp.route('/', methods=['GET'])
def get_faults():
    faults = Fault.query.all()
    return jsonify([{
        'id': f.id,
        'student_id': f.student_id,
        'description': f.description,
        'date_reported': f.date_reported.strftime('%Y-%m-%d'),
        'resolved': f.resolved
    } for f in faults]), 200

# Update a fault (PUT)
@faults_bp.route('/<int:fault_id>', methods=['PUT'])
def update_fault(fault_id):
    fault = Fault.query.get_or_404(fault_id)
    data = request.get_json()
    fault.description = data.get('description', fault.description)
    fault.resolved = data.get('resolved', fault.resolved)
    db.session.commit()
    return jsonify({'message': 'Fault updated'}), 200

# Delete a fault (DELETE)
@faults_bp.route('/<int:fault_id>', methods=['DELETE'])
def delete_fault(fault_id):
    fault = Fault.query.get_or_404(fault_id)
    db.session.delete(fault)
    db.session.commit()
    return jsonify({'message': 'Fault deleted'}), 200
