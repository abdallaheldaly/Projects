# Use PHP with Apache as base image
FROM php:7.4-apache

# Update package repositories and install required dependencies
RUN apt-get update && apt-get install -y \
    libzip-dev \
    zip \
    && docker-php-ext-install zip pdo pdo_mysql

# Copy application files to the container's working directory
COPY . /var/www/html/

# Set working directory
WORKDIR /var/www/html

# Enable Apache mod_rewrite
RUN a2enmod rewrite

# Set proper permissions for application directory
RUN chown -R www-data:www-data /var/www/html

# Environment variables for database configuration
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=task_management
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password

# Expose Apache port
EXPOSE 80

# Start Apache service when container runs
CMD ["apache2-foreground"]