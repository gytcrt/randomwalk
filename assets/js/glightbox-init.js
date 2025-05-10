// Initialize GLightbox with enhanced modal options
document.addEventListener('DOMContentLoaded', function() {
  const lightbox = GLightbox({
    // General settings
    selector: '.glightbox',
    touchNavigation: true,
    loop: true,
    autoplayVideos: true,
    preload: false,
    
    // Modal-specific settings
    openEffect: 'zoom',     // Options: 'zoom', 'fade', 'none'
    closeEffect: 'fade',    // Options: 'zoom', 'fade', 'none'
    slideEffect: 'slide',   // Options: 'slide', 'fade', 'zoom', 'none'
    
    // Overlay settings
    moreText: 'View more',
    closeButton: true,      // Show close button
    
    // Navigation
    keyboardNavigation: true,
    arrows: true,           // Show navigation arrows
    
    // Caption/Description
    draggable: true,
    
    // Dimensions
    width: '90vw',          // Default width for content
    height: 'auto',         // Default height for content
    
    // Mobile settings
    descPosition: 'bottom', // Position of the descriptions (bottom or top)
    
    // Customization options
    cssEffects: {
      fade: { in: 'fadeIn', out: 'fadeOut' },
      zoom: { in: 'zoomIn', out: 'zoomOut' },
      slide: { in: 'slideInRight', out: 'slideOutLeft' }
    },
    
    // Events
    onOpen: () => {
      // Function to execute when lightbox is opened
    },
    onClose: () => {
      // Function to execute when lightbox is closed
    }
  });
}); 