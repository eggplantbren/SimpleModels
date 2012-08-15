/*
* Copyright (c) 2009, 2010, 2011, 2012 Brendon J. Brewer.
*
* This file is part of DNest3.
*
* DNest3 is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
*
* DNest3 is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with DNest3. If not, see <http://www.gnu.org/licenses/>.
*/

#include <iostream>
#include "Start.h"
#include "Data.h"
#include "FitLine.h"

using namespace std;
using namespace DNest3;

int main(int argc, char** argv)
{
	// Process command line options and load data
	CommandLineOptions options(argc, argv);
	string dataFile = options.get_dataFile();
	if(dataFile.compare("") == 0)
		Data::get_instance().load("../emission_line_data.txt");
	else
		Data::get_instance().load(dataFile.c_str());

	// Initialise the sampler
	#ifndef DNest3_No_Boost
	MTSampler<FitLine> sampler = setup_mt<FitLine>(options);
	#else
	Sampler<FitLine> sampler = setup<FitLine>(options);
	#endif

	// Go!
	sampler.run();

	return 0;
}

