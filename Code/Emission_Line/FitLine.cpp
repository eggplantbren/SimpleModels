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

#include "FitLine.h"
#include "RandomNumberGenerator.h"
#include "Utils.h"
#include "Data.h"
#include <cmath>
#include <iostream>

using namespace std;
using namespace DNest3;

FitLine::FitLine()
{

}

void FitLine::fromPrior()
{
	A = exp(log(1E-3) + log(1E6)*randomU());
	c = -10. + 20.*randomU();
	w = exp(log(1E-3) + log(1E6)*randomU());
}

double FitLine::perturb()
{
	double logH = 0.;
	
	if(randomU() <= 0.33333)
	{
		A = log(A);
		A += log(1E6)*pow(10., 1.5 - 6*randomU())*randn();
		A = mod(A - log(1E-3), log(1E6)) + log(1E-3);
		A = exp(A);
	}
	else if(randomU() <= 0.5)
	{
		c += 20*pow(10., 1.5 - 6*randomU())*randn();
		c = mod(c + 10., 20.) - 10.;
	}
	else
	{
		w = log(w);
		w += log(1E6)*pow(10., 1.5 - 6*randomU())*randn();
		w = mod(w - log(1E-3), log(1E6)) + log(1E-3);
		w = exp(w);
	}

	return logH;
}

double FitLine::logLikelihood() const
{
	double mock;
	double chisq = 0.;
	for(int i=0; i<Data::get_instance().get_N(); i++)
	{
		mock = A*exp(-0.5*pow((Data::get_instance().get_x(i) - c)/w, 2));
		chisq += pow((Data::get_instance().get_y(i) - mock)/Data::get_instance().get_sig(i), 2);
	}

	return -0.5*chisq;
}


void FitLine::print(std::ostream& out) const
{
	out<<A<<' '<<c<<' '<<w<<' ';
}

string FitLine::description() const
{
	string result("A, c, w");
	return result;
}


