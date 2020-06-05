import sys

from docxtpl import DocxTemplate
sys.path.insert(0, '/home/mvlab/belresusrs')
data_act={
        'act_number': '001', 'date': '01.01.2020', 'time': '00:00',
        'position01':'pos01', 'name01':'name01',
        'position02': '', 'name02': '',
        'position03': '', 'name03': '',
        'position04': '', 'name04': '',
        'seller_name': 'seller_name',
        'seller_addres': 'seller_addres',
        'number_date_contract': 'number_date_contract',
        'contract_date': 'contract_date',
        'type_transport':'type_transport',
        'number_transport':'number_transport',
        'type_documents':'type_documents',
        'number_documents': 'number_documents',
        'date_documents': 'number_documents',
        'date_arrival': 'number_documents',
        'weight_consignment': 'weight_consignment',
        'weight_transport_with_cargo':'weight_transport_with_cargo',
        'weight_transport_without_cargo': 'weight_transport_without_cargo',
        'actual_weight': 'actual_weight',
        'weight_deficit': 'weight_deficit',
        'weediness': 'weediness',
        'load_weight': 'load_weight'
}
def redactDocx(path_to_shablon, path_to_save_docx, Data,response ):
    '''изменяет шаблон документа doc'''
    doc = DocxTemplate(path_to_shablon)
    context = {
        'act_number': Data['act_number'],
        'date': Data['date'], 'time': Data['time'],
        'position01': Data['position01'], 'name01':Data['name01'],
        'position02': Data['position02'], 'name02': Data['name02'],
        'position03': Data['position03'], 'name03': Data['name03'],
        'position04': Data['position04'], 'name04': Data['name04'],
        'seller_name': Data['seller_name'],
        'seller_addres': Data['seller_addres'],
        'number_date_contract': Data['number_date_contract'],
        'contract_date': Data['contract_date'],
        'type_transport':Data['type_transport'],
        'number_transport':Data['number_transport'],
        'type_documents':Data['type_documents'],
        'number_documents': Data['number_documents'],
        'date_documents': Data['date_documents'],
        'date_arrival': Data['date_arrival'],
        'weight_consignment': Data['weight_consignment'],
        'weight_transport_with_cargo':Data['weight_transport_with_cargo'],
        'weight_transport_without_cargo': Data['weight_transport_without_cargo'],
        'actual_weight': Data['actual_weight'],
        'weight_deficit': Data['weight_deficit'],
        'weediness': Data['weediness'],
        'load_weight': Data['load_weight']
    }

    doc.render(context)
    return doc.save(response)


if __name__ == '__main__':
    # createAkt('doc001.docx')

    redactDocx('ШАБЛОН Акт приемки смешанного стеклобоя.docx', 'res001.docx', data_act)
