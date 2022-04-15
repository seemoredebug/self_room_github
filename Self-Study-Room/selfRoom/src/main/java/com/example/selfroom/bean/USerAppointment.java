package com.example.selfroom.bean;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class USerAppointment {
    private String reservationNumber;
    private String seatNumber;
    private String timequantum;
    private String remark;
    private String score;
    private int used;
}
