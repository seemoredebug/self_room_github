package com.example.selfroom.control;

import com.example.selfroom.bean.UsageRecord;
import com.example.selfroom.service.SysFunctionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SysFunctionControl {
    @Autowired
    SysFunctionService sysFunctionService;

    @RequestMapping("/addSA")//预约
    public boolean addUSerAppointment(UsageRecord usageRecord,String remark){//预约
        return sysFunctionService.addUSerAppointment(usageRecord, remark);
    }

    @RequestMapping("/dropSA")//取消预约
    public boolean dropUSerAppointment(String reservationNumber){//取消预约
        return sysFunctionService.dropUSerAppointment(reservationNumber);
    }
}
