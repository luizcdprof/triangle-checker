import pytest
import triangle

def test_validate_triangle_sides():
    # Triângulo retângulo
    assert triangle.validate_sides(3, 4, 5)

    # Triângulo equilátero
    assert triangle.validate_sides(5, 5, 5)
    
    # Triângulo isósceles
    assert triangle.validate_sides(5, 5, 8)

    # Triângulos inválidos
    assert not triangle.validate_sides(1, 1, 3)
    assert not triangle.validate_sides(0, 0, 0)
    assert not triangle.validate_sides(-1, 2, 3)

def test_validate_triangle_angles():
    # Triângulo acutângulo (agudo)
    assert triangle.validate_angles(60, 60, 60)

    # Triângulo retângulo
    assert triangle.validate_angles(90, 45, 45)
    
    # Triângulo obtusângulo (obtuso)
    assert triangle.validate_angles(100, 40, 40)

    # Triângulos inválidos
    assert not triangle.validate_angles(90, 90, 90)
    assert not triangle.validate_angles(0, 0, 0)
    assert not triangle.validate_angles(-30, 60, 150)