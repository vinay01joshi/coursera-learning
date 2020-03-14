import math

def traiange(base, height):
	return base * height / 2

def rectange(base, height):
	return base * height

def circle(radius):
	return math.pi * (radius ** 2)

def donut(outer_radius, inner_radius):
	return circle(outer_radius) - circle(inner_radius)