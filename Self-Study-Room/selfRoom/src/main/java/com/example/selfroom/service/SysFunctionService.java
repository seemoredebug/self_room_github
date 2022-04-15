package com.example.selfroom.service;

import com.example.selfroom.bean.USerAppointment;
import com.example.selfroom.bean.UsageRecord;
import com.example.selfroom.mappers.SysFunctionMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;



//预约

@Service
public class SysFunctionService {
    @Autowired
    SysFunctionMapper sysFunctionMapper;
    @Autowired
    SeatInformationService seatInformationService;
    @Autowired
    UserDataService userDataService;

    public boolean addUSerAppointment(UsageRecord usageRecord,String remark){//预约
        if(seatInformationService.getOneUsageRecord(usageRecord.getRecordNumber())==0){//没有座位使用记录
            seatInformationService.insertUsageRecord(usageRecord);

            String reservationNumber ;
            reservationNumber= usageRecord.getSeatTime().substring(0,8);//时间
            reservationNumber+= usageRecord.getScore().substring(0,4);//班级
            reservationNumber+=usageRecord.getScore().substring(10);//学号
            int cr = sysFunctionMapper.countUSerAppointmentByData(usageRecord.getSeatTime().substring(0,8)+"%");
            if(cr<10){
                reservationNumber+="0";
            }
            cr++;
            reservationNumber+=cr;
            USerAppointment uSerAppointment=new USerAppointment(reservationNumber,
                                            usageRecord.getRoomNumber(),
                                            usageRecord.getSeatTime(),remark,usageRecord.getScore(),0);
            sysFunctionMapper.addUSerAppointment(uSerAppointment);
            return true;

        }
        return false;
    }

    public boolean dropUSerAppointment(String reservationNumber){//取消预约
        try {
            USerAppointment uSerAppointment=userDataService.getoUSerAppointmentBynumber(reservationNumber);
            UsageRecord usageRecord=new UsageRecord();
            usageRecord.setSeatTime(uSerAppointment.getTimequantum());
            usageRecord.setScore(uSerAppointment.getScore());
            seatInformationService.dropUsageRecord(usageRecord);
            sysFunctionMapper.dropUSerAppointment(reservationNumber);
            return true;
        }catch (Exception  e){
            return false;
        }


    }
}
