// Generated automatically via PyRTL
// As one initial test of synthesis, map to FPGA with:
//   yosys -p "synth_xilinx -top toplevel" thisfile.v

module toplevel(clk, rst, alpha, gamma, max_q_next, q, r, q_new);
    input clk;
    input rst;
    input[15:0] alpha;
    input[15:0] gamma;
    input[15:0] max_q_next;
    input[15:0] q;
    input[15:0] r;
    output[31:0] q_new;

    wire const_0_0;
    wire const_1_0;
    wire const_2_0;
    wire const_3_0;
    wire const_4_0;
    wire const_5_0;
    wire[31:0] tmp0;
    wire[21:0] tmp1;
    wire[9:0] tmp2;
    wire[31:0] tmp3;
    wire[15:0] tmp4;
    wire[31:0] tmp5;
    wire[32:0] tmp6;
    wire[16:0] tmp7;
    wire[32:0] tmp8;
    wire[33:0] tmp9;
    wire[17:0] tmp10;
    wire[33:0] tmp11;
    wire[67:0] tmp12;
    wire[57:0] tmp13;
    wire[9:0] tmp14;
    wire[67:0] tmp15;
    wire[51:0] tmp16;
    wire[67:0] tmp17;
    wire[68:0] tmp18;
    wire[31:0] tmp19;

    // Combinational
    assign const_0_0 = 0;
    assign const_1_0 = 0;
    assign const_2_0 = 0;
    assign const_3_0 = 0;
    assign const_4_0 = 0;
    assign const_5_0 = 0;
    assign q_new = tmp19;
    assign tmp0 = gamma * max_q_next;
    assign tmp1 = {tmp0[31], tmp0[30], tmp0[29], tmp0[28], tmp0[27], tmp0[26], tmp0[25], tmp0[24], tmp0[23], tmp0[22], tmp0[21], tmp0[20], tmp0[19], tmp0[18], tmp0[17], tmp0[16], tmp0[15], tmp0[14], tmp0[13], tmp0[12], tmp0[11], tmp0[10]};
    assign tmp2 = {const_0_0, const_0_0, const_0_0, const_0_0, const_0_0, const_0_0, const_0_0, const_0_0, const_0_0, const_0_0};
    assign tmp3 = {tmp2, tmp1};
    assign tmp4 = {const_1_0, const_1_0, const_1_0, const_1_0, const_1_0, const_1_0, const_1_0, const_1_0, const_1_0, const_1_0, const_1_0, const_1_0, const_1_0, const_1_0, const_1_0, const_1_0};
    assign tmp5 = {tmp4, r};
    assign tmp6 = tmp5 + tmp3;
    assign tmp7 = {const_2_0, const_2_0, const_2_0, const_2_0, const_2_0, const_2_0, const_2_0, const_2_0, const_2_0, const_2_0, const_2_0, const_2_0, const_2_0, const_2_0, const_2_0, const_2_0, const_2_0};
    assign tmp8 = {tmp7, q};
    assign tmp9 = tmp6 - tmp8;
    assign tmp10 = {const_3_0, const_3_0, const_3_0, const_3_0, const_3_0, const_3_0, const_3_0, const_3_0, const_3_0, const_3_0, const_3_0, const_3_0, const_3_0, const_3_0, const_3_0, const_3_0, const_3_0, const_3_0};
    assign tmp11 = {tmp10, alpha};
    assign tmp12 = tmp11 * tmp9;
    assign tmp13 = {tmp12[67], tmp12[66], tmp12[65], tmp12[64], tmp12[63], tmp12[62], tmp12[61], tmp12[60], tmp12[59], tmp12[58], tmp12[57], tmp12[56], tmp12[55], tmp12[54], tmp12[53], tmp12[52], tmp12[51], tmp12[50], tmp12[49], tmp12[48], tmp12[47], tmp12[46], tmp12[45], tmp12[44], tmp12[43], tmp12[42], tmp12[41], tmp12[40], tmp12[39], tmp12[38], tmp12[37], tmp12[36], tmp12[35], tmp12[34], tmp12[33], tmp12[32], tmp12[31], tmp12[30], tmp12[29], tmp12[28], tmp12[27], tmp12[26], tmp12[25], tmp12[24], tmp12[23], tmp12[22], tmp12[21], tmp12[20], tmp12[19], tmp12[18], tmp12[17], tmp12[16], tmp12[15], tmp12[14], tmp12[13], tmp12[12], tmp12[11], tmp12[10]};
    assign tmp14 = {const_4_0, const_4_0, const_4_0, const_4_0, const_4_0, const_4_0, const_4_0, const_4_0, const_4_0, const_4_0};
    assign tmp15 = {tmp14, tmp13};
    assign tmp16 = {const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0, const_5_0};
    assign tmp17 = {tmp16, q};
    assign tmp18 = tmp17 + tmp15;
    assign tmp19 = {tmp18[31], tmp18[30], tmp18[29], tmp18[28], tmp18[27], tmp18[26], tmp18[25], tmp18[24], tmp18[23], tmp18[22], tmp18[21], tmp18[20], tmp18[19], tmp18[18], tmp18[17], tmp18[16], tmp18[15], tmp18[14], tmp18[13], tmp18[12], tmp18[11], tmp18[10], tmp18[9], tmp18[8], tmp18[7], tmp18[6], tmp18[5], tmp18[4], tmp18[3], tmp18[2], tmp18[1], tmp18[0]};

endmodule

