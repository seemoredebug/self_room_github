package com.example.selfroom.mappers;

import com.example.selfroom.bean.USerAppointment;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface SysFunctionMapper {
    public void addUSerAppointment(USerAppointment uSerAppointment);
    public int countUSerAppointmentByData(String timequantum);
    public void dropUSerAppointment(String reservationNumber);
}
