package com.example.selfroom.mappers;


import com.example.selfroom.bean.USerAppointment;
import com.example.selfroom.bean.UsageRecord;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface UsageRecordMapper {
    public List<UsageRecord> getUsageRecord(String room);
    public int getOneUsageRecord(String recordNumber);
    public void insertUsageRecord(UsageRecord usageRecord);
    public void dropUsageRecord(UsageRecord usageRecord);
}
