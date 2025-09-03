#!/usr/bin/env python3
"""
Portfolio Update Script
======================

Quick and easy way to update your Me-API Playground portfolio.

Usage:
    python update_portfolio.py
"""

import subprocess
import sys
import os

def run_command(cmd):
    """Run a command and return the result."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def update_portfolio():
    """Update the portfolio with new data."""
    print("🚀 Portfolio Update Script")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists("seed_data.py"):
        print("❌ Error: seed_data.py not found!")
        print("Please run this script from your project root directory.")
        return False
    
    # Update the database
    print("📊 Updating portfolio database...")
    success, stdout, stderr = run_command("python seed_data.py")
    
    if success:
        print("✅ Database updated successfully!")
        print(stdout)
        
        # Check if we're in a git repository
        if os.path.exists(".git"):
            print("\n📝 Git repository detected.")
            
            # Ask user if they want to commit and push
            commit = input("Do you want to commit and push changes to deploy? (y/n): ").lower().strip()
            
            if commit in ['y', 'yes']:
                print("\n🔄 Committing changes...")
                
                # Add files
                run_command("git add .")
                
                # Commit with a message
                commit_msg = input("Enter commit message (or press Enter for default): ").strip()
                if not commit_msg:
                    commit_msg = "Update portfolio data"
                
                success, _, _ = run_command(f'git commit -m "{commit_msg}"')
                
                if success:
                    print("✅ Changes committed!")
                    
                    # Push to remote
                    print("🚀 Pushing to remote repository...")
                    success, _, stderr = run_command("git push")
                    
                    if success:
                        print("✅ Changes pushed successfully!")
                        print("🌐 Your portfolio will be updated on Render shortly.")
                        print("📍 Live URL: https://me-api-playground-1-sutg.onrender.com/static/index.html")
                    else:
                        print(f"❌ Failed to push: {stderr}")
                else:
                    print("❌ Failed to commit changes.")
            else:
                print("📝 Changes saved locally. Run 'git add . && git commit && git push' to deploy.")
        else:
            print("📝 Portfolio updated locally!")
            
        return True
    else:
        print(f"❌ Failed to update database: {stderr}")
        return False

def show_help():
    """Show help information."""
    print("📚 Portfolio Management Help")
    print("=" * 40)
    print("To update your portfolio:")
    print("1. Edit the configuration in seed_data.py")
    print("2. Run: python update_portfolio.py")
    print("3. Follow the prompts to deploy")
    print()
    print("Available commands:")
    print("  python seed_data.py stats  - Show portfolio statistics")
    print("  python seed_data.py help   - Show seed_data help")
    print()
    print("Configuration sections to edit in seed_data.py:")
    print("  • PROFILE_CONFIG - Your personal information")
    print("  • EDUCATION_CONFIG - Your education history")
    print("  • SKILLS_CONFIG - Your technical skills")
    print("  • PROJECTS_CONFIG - Your projects portfolio")
    print("  • WORK_CONFIG - Your work experience")
    print("  • LINKS_CONFIG - Your social media links")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "help":
        show_help()
    else:
        update_portfolio()