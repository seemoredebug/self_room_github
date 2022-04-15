package com.example.selfroom.mappers;

import com.example.selfroom.bean.USerAppointment;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;


@Mapper
public interface USerAppointmentMapper {
    public List<USerAppointment> getUSerAppointment(String score);
    public  List<USerAppointment> getNoUSerAppointment(String score);
    public  void deleNoUSerAppointment(String Number);
    public  USerAppointment getoUSerAppointmentBynumber(String number);
    public int countUSerAppointment(String score);
    public int countNoUSerAppointment(String score);
}
