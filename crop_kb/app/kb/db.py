from .models import Crop, Ftime, Ftype, Farming, Session
from .knowledge_dict import knowledge, CROPS, FTIME, FTYPE


def insert_item(item):
    '''写数据库'''
    session = Session()
    try:
        session.add(item)
        session.commit()
    except Exception as e:
        print('数据写入数据库出错，错误原因{}'.format(e))
        session.rollback()
    session.close()

def get_fdetail():
    crops_dict = dict(CROPS)
    ftime_dict = dict(FTIME)
    ftype_dict = dict(FTYPE)
    k_crops = knowledge['作物']
    crops = k_crops.keys()
    for crop in crops:
        crop_id = crops_dict.get(crop)
        k_crop_times = k_crops[crop]['时间']
        times = k_crop_times.keys()
        for time in times:
            ftime_id = ftime_dict.get(time)
            k_crop_time_farms = k_crop_times[time].get('农事')
            if k_crop_time_farms:
                farms = k_crop_time_farms.keys()
                for farm in farms:
                    ftype_id = ftype_dict.get(farm)
                    k_crop_time_farm_fds = k_crop_time_farms[farm]
                    print(' '.join(k_crop_time_farm_fds))
                    d = Farming(fdetail=' '.join(k_crop_time_farm_fds),
                                crop_id=crop_id,
                                ftime_id=ftime_id,
                                ftype_id=ftype_id
                                )
                    insert_item(d)


def get():
    for ftype in FTYPE:
        c = Ftype(ftype_id=ftype[1], ftype=ftype[0])
        insert_item(c)



if __name__ == '__main__':
    get()
    get_fdetail()

