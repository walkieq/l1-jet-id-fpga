#ifndef DEFINES_H_
#define DEFINES_H_

#include "ap_int.h"
#include "ap_fixed.h"
#include "../nnet_utils/nnet_types.h"

// add macros e.g #define
#define P 3 // change to 16, set to 2 for testing
#define N_o 8
#define N_e (N_o * (N_o - 1))
#define D_e 6
#define D_o 6

// DNN1
//#define N_INPUT_1_1 P
#define N_LAYER_2 12
#define N_OUTPUT_1 D_e

//#define N_LAYER_4 25
#define N_LAYER_6 36
#define N_LAYER_8 18
#define N_OUTPUT_2 D_o

//#define N_INPUT_1_2 N_o

#define N_LAYER_10 170
//#define N_LAYER_12 24
#define N_OUTPUT_3 5 // number of jet classes

// reuse factor
//#define RO 1;
//#define DPP 1;

#define RO  1;
#define DPP 7; // only used to show the real number of fR, not used in the custom FSM  


#define R1 1;
#define R2 RO;
#define R3 RO;



// add types e.g typedef ap_fixed<24,12> input_t

#define bits_total 12
#define bits_integer 4


typedef ap_fixed<bits_total, bits_integer> model_default_t; 
//typedef model_default_t model_params_t; 

typedef ap_uint<6> jedi_r_id_t;
typedef ap_fixed<16,6> jedi_accum_t;


typedef model_default_t result_t;
typedef model_default_t itmdia_t;
typedef model_default_t input_t; // default <16,6>, changed to <16,10>

typedef ap_fixed<8, 1> model_params_t; 


//typedef ap_fixed<8, 1> weight30_t;
//typedef ap_fixed<8, 1> bias30_t;
//typedef ap_fixed<8, 1> weight31_t;
//typedef ap_fixed<8, 1> bias31_t;
//
//typedef ap_fixed<8, 1> weight32_t;
//typedef ap_fixed<8, 1> bias32_t;
//typedef ap_fixed<8, 1> weight33_t;
//typedef ap_fixed<8, 1> bias33_t;
//typedef ap_fixed<8, 1> weight34_t;
//typedef ap_fixed<8, 1> bias34_t;
//
//typedef ap_fixed<8, 1> weight24_t;
//typedef ap_fixed<8, 1> bias24_t;
//typedef ap_fixed<8, 1> weight27_t;
//typedef ap_fixed<8, 1> bias27_t;


typedef model_params_t fc1_weight_t;
typedef model_params_t fc1_bias_t;
typedef model_params_t fc3_weight_t;
typedef model_params_t fc3_bias_t;

typedef model_params_t fc4_weight_t;
typedef model_params_t fc4_bias_t;
typedef model_params_t fc5_weight_t;
typedef model_params_t fc5_bias_t;
typedef model_params_t fc6_weight_t;
typedef model_params_t fc6_bias_t;

typedef model_params_t fc7_weight_t;
typedef model_params_t fc7_bias_t;
typedef model_params_t fc9_weight_t;
typedef model_params_t fc9_bias_t;


#endif
