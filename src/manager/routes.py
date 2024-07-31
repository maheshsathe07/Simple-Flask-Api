from flask import Blueprint, jsonify, request
from model.models import db, SampleTable
from utility.utils import setup_logger

api = Blueprint('api', __name__)

get_sample_logger = setup_logger('get_sample')
add_sample_logger = setup_logger('add_sample')

@api.route('/samples', methods=['GET'])
def get_samples():
    sample_id = request.args.get('id') 
    if sample_id:
        try:
            sample = SampleTable.query.get(sample_id) 
            if sample:
                get_sample_logger.info(f'Sample with id {sample_id} fetched successfully')
                return jsonify({'id': sample.id, 'name': sample.name, 'age': sample.age})
            else:
                get_sample_logger.warning(f'Sample with id {sample_id} not found')
                return jsonify({'error': 'Sample not found'}), 404
        except Exception as e:
            get_sample_logger.error(f"Error fetching sample with id {sample_id}: {e}")
            return jsonify({"error": "Error fetching sample"}), 500
    else:
        try:
            samples = SampleTable.query.all()
            get_sample_logger.info('All samples fetched successfully')
            return jsonify([{'id': sample.id, 'name': sample.name, 'age': sample.age} for sample in samples])
        except Exception as e:
            get_sample_logger.error(f"Error fetching samples: {e}")
            return jsonify({"error": "Error fetching samples"}), 500

@api.route('/samples', methods=['POST'])
def add_sample():
    try:
        data = request.get_json()
        new_sample = SampleTable(name=data['name'], age=data['age'])
        db.session.add(new_sample)
        db.session.commit()
        # Log successful data addition
        add_sample_logger.info('Sample added successfully')
        return jsonify({'message': 'Sample added successfully'}), 201
    except Exception as e:
        add_sample_logger.error(f"Error adding sample: {e}")
        return jsonify({"error": "Error adding sample"}), 500
