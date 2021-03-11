pragma solidity ^0.5.0;

import "arcadeTokenMintable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";

contract Investors {
    
    address payable investor_one;
    string equityOne = "TSLA";
    uint price;
    bool is_buy_order;
    
}

contract Investment is ERC721{
    
	mapping(address => uint) tokens;
	
	function approval(address _owner, address _approved,uint _tokenId) {
		require(tokens[_owner]==_tokenId);
		
		tokens[_approved]=_tokenId;
	}
	
		function transfer(address _to, uint _amount) payable{
		require(_amount <= tokens[msg.sender]);
		tokens[msg.sender]-=_amount;
		tokens[_to]+=_amount;
	}
	
	function balanceOf(address _owner) view returns (uint){
		return tokens[_owner];
		
	}
	
	function ownerOf(uint _tokenId) view returns(address){
		return tokens[_id].address;
		
	}
	
	function TransferFrom(address _from, address _to, uint _tokenId) payable{
		require(tokens[_from]==_tokenId);
		tokens[_from]=0;
		tokens[_to]=_tokenId;
		
	}
	
	function approve(address _approved, uint _tokenId) payable{
		require(tokens[msg.sender]==_tokenId);
		tokens[_approved]=_tokenId;
		
	}
	
	function mint(address _to, uint _tokenId) {
		tokens[_to] = 'mytoken '+str(uint(blockhash(block.number - 1)));
		
	}
	
}