from ..models import Measurement
from ..models import Variable
def get_measurements():
    measurments = Measurement.objects.all()
    return measurments

def get_measurement(var_pk):
    measurment = Measurement.objects.get(pk=var_pk)
    return measurment

def update_measurement(mea_pk, new_mea):
    measurment = get_measurement(mea_pk)
    measurment.place = new_mea["place"]
    measurment.value = new_mea["value"]
    measurment.unit = new_mea["unit"]
    measurment.Variable = Variable.objects.get(pk = new_mea["variable"])
    measurment.save()
    return measurment

def create_measurement(var):
    measurment = Measurement(
        place=var["place"],
        value = var["value"],
        unit = var["unit"],
        variable = Variable.objects.get(pk = var["variable"])
        )
    measurment.save()
    return measurment
def delete_measurement(mea_pk):
    measument = get_measurement(mea_pk)
    measument.delete()
    