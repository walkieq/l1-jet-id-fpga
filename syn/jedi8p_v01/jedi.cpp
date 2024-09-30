//
//    rfnoc-hls-neuralnet: Vivado HLS code for neural-net building blocks
//
//    Copyright (C) 2017 EJ Kreinar
//
//    This program is free software: you can redistribute it and/or modify
//    it under the terms of the GNU General Public License as published by
//    the Free Software Foundation, either version 3 of the License, or
//    (at your option) any later version.
//
//    This program is distributed in the hope that it will be useful,
//    but WITHOUT ANY WARRANTY; without even the implied warranty of
//    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//    GNU General Public License for more details.
//
//    You should have received a copy of the GNU General Public License
//    along with this program.  If not, see <http://www.gnu.org/licenses/>.
//
#include <iostream>

#include "jedi.h"
#include "../nnet_utils/nnet_jedi.h"

#include "weights8p/w1.h"
#include "weights8p/w2.h"
#include "weights8p/b1.h"
#include "weights8p/b2.h"

#include "weights8p/w4.h"
#include "weights8p/w5.h"
#include "weights8p/w6.h"
#include "weights8p/b4.h"
#include "weights8p/b5.h"
#include "weights8p/b6.h"

#include "weights8p/w7.h"
//#include "weights8p/w8.h"
#include "weights8p/w9.h"
#include "weights8p/b7.h"
//#include "weights8p/b8.h"
#include "weights8p/b9.h"


void jedi(
	    input_t I[N_o][P], // change to number of particles
        result_t result[N_OUTPUT_3]
    ){
        #pragma HLS DATAFLOW
        
        #pragma HLS ARRAY_PARTITION variable=I       complete dim=2
        #pragma HLS ARRAY_PARTITION variable=I       complete dim=1

        input_t O[N_o][D_o];

        nnet::jedi_pi_2layer<input_t, input_t, jedi_config, dense1_config, dense2_config>(I, O, w1, w2, b1, b2, w4, w5, w6, b4, b5, b6);
        //nnet::jedi_fusion_dnn1_2layer<input_t, input_t, jedi_config, dense1_config, dense2_config>(I, O, w1, w2, b1, b2, w4, w5, w6, b4, b5, b6);
		
        nnet::jedi_dnn3_mlst01<input_t, input_t, dense3_config>(O, result, w7, w9, b7, b9);
        
}
