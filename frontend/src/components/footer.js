import React from "react";
import "./footer.css";

const Footer = () => {
    return (
        <footer className="footer">
            <div className="footer-container">
                <div className="footer-left">
                    <p>&copy; 2024 Brainstormer. All rights reserved.</p>
                </div>
                <div className="footer-right">
                    <a href="/privacy" className="footer-link">
                        Privacy Policy
                    </a>
                    <a href="/terms" className="footer-link">
                        Terms of Service
                    </a>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
