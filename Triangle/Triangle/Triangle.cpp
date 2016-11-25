// triangle.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <vector>
#include <string>
#include <algorithm>
#include <regex>
#include <iostream>
#include <Windows.h>

enum ARGUMENTS_ERROR { NO = 0, COUNT, FORMAT, VALUE, };

bool IsCorrect(const char* number)
{
	std::regex double_reg_exp("(\\+|-)?((0)|([1-9][0-9]*))(\\.[0-9]+)?");
	return std::regex_match(number, double_reg_exp);
}

ARGUMENTS_ERROR HandleParams(int argc, char* argv[], std::vector<double> & sides)
{
	if (argc != 4)
	{
		return COUNT;
	}

	std::vector<double> temp_sides;

	for (size_t i = 1; i < 4; ++i)
	{
		if (!(IsCorrect(argv[i])))
		{
			return FORMAT;
		}
		temp_sides.push_back(std::stod(argv[i]));
	}

	for (size_t i = 0; i < temp_sides.size(); ++i)
	{
		if (temp_sides[i] <= 0)
		{
			return VALUE;
		}
	}

	sides = temp_sides;
	return NO;
}


class CTriangle
{
public:
	CTriangle(double a, double b, double c)
	{
		if (a <= 0 || b <= 0 || c <= 0)
		{
			return;
		}

		if (a + b <= c || a + c <= b || c + b <= a)
		{
			return;
		}

		m_a = a;
		m_b = b;
		m_c = c;
	}

	std::string GetType() const
	{
		if (m_a < 0)
		{
			return "не треугольник";
		}

		if (fabs(m_a - m_b) < EPS && fabs(m_a - m_c) < EPS)
		{
			return "равносторонний";
		}

		if (fabs(m_a - m_b) < EPS || fabs(m_a - m_c) < EPS || fabs(m_b - m_c) < EPS)
		{
			return "равнобедренный";
		}

		return "обычный";
	}

private:
	double m_a = -1.0;
	double m_b = -1.0;
	double m_c = -1.0;
	const double EPS = 1e-5;

};


int main(int argc, char* argv[])
{
	SetConsoleCP(1251);
	SetConsoleOutputCP(1251);


	std::vector<double> sides;
	auto ERR = HandleParams(argc, argv, sides);

	if (ERR == COUNT)
	{
		std::cout << "Введите 3 стороны" << std::endl;
		return ERR;
	}
	else if (ERR == FORMAT)
	{
		std::cout << "Стороны должны быть числами" << std::endl;
		return ERR;
	}
	else if (ERR == VALUE)
	{
		std::cout << "Числа должны быть положительными" << std::endl;
		return ERR;
	}
	CTriangle triangle(sides[0], sides[1], sides[2]);
	std::cout << triangle.GetType() << std::endl;
	return ERR;
}
